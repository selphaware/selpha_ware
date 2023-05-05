import os
import boto3
import zipfile
from typing import List
import io
import base64
from urllib.parse import parse_qs


def download_and_extract_library(bucket_name, library_key):
    s3 = boto3.client('s3')
    library_zip = '/tmp/library.zip'
    s3.download_file(bucket_name, library_key, library_zip)

    with zipfile.ZipFile(library_zip, 'r') as zip_ref:
        zip_ref.extractall('/tmp')
    os.remove(library_zip)


def install_libs(bucket_name: str, libs: List[str]) -> None:
    library_keys = [f"tmp/library_with_deps_{x}.zip" for x in libs]

    for library_key in library_keys:
        print(f"downloading and extracting from S3: {library_key}")
        download_and_extract_library(bucket_name, library_key)


def extract_csv_to_dataframe(main_val, pd):
    # Split the lines in main_val
    lines = main_val.split('\n')

    # Find the index of the line containing the CSV header
    csv_start_index = None
    for i, line in enumerate(lines):
        if 'Content-Type: text/csv' in line:
            csv_start_index = i + 1
            break

    # Extract the CSV data and join it with newline characters
    csv_data = '\n'.join(lines[csv_start_index:-1])

    # Create a StringIO object with the CSV data
    csv_buffer = io.StringIO(csv_data)

    # Read the CSV data into a DataFrame
    df = pd.read_csv(csv_buffer)

    return df


def get_data_from_body(event):
    if event['isBase64Encoded']:
        event['body'] = base64.b64decode(event['body']).decode('utf-8')
    # Parse the POST request and extract the uploaded CSV file
    lowercase_headers = {k.lower(): v for k, v in event['headers'].items()}
    content_type = lowercase_headers['content-type']
    print(f"content-type: {content_type}")
    print(f"content: {event['body']}")
    post_data = parse_qs(event['body'], keep_blank_values=True)
    print(f"post_data: {post_data}")
    print(f"type(post_data): {type(post_data)}")
    post_data_content = list(post_data.values())
    print(f"post_data_content: {post_data_content[0]}")
    print(f"post_data_content_type: {type(post_data_content[0])}")
    print(f"post_data_content_LEN: {len(post_data_content[0])}")
    main_val = post_data_content[0][0]

    return main_val
