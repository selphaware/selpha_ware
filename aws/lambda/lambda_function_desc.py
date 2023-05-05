import io
import base64
import sys
from util.lamutil import (
    install_libs,
    extract_csv_to_dataframe,
    get_data_from_body
)


def lambda_handler(event, context):
    if event['httpMethod'] == 'GET':
        return serve_html_page()
    elif event['httpMethod'] == 'POST':
        return process_csv(event)


def serve_html_page():
    html = '''
    <html>
        <head>
            <title>Data Description (Pandas) Tool</title>
            <style>
                body {
                    background-color: #2c3e50;
                    color: #ecf0f1;
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                form {
                    text-align: center;
                }
                input[type="file"] {
                    color: #ecf0f1;
                }
                input[type="submit"] {
                    background-color: #3498db;
                    border: none;
                    color: #ecf0f1;
                    padding: 10px 20px;
                    text-decoration: none;
                    margin: 4px 2px;
                    cursor: pointer;
                    font-size: 16px;
                }
            </style>
        </head>
        <body>
            <form action="" method="post" enctype="multipart/form-data">
                <h1>Upload CSV</h1>
                <input type="file" name="csv_file" accept=".csv"><br><br>
                <input type="submit" value="Upload and Analyze">
            </form>
        </body>
    </html>
    '''
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/html'},
        'body': html
    }


def process_csv(event):
    bucket_name = 'edaprof'
    libraries = ['pandas', 'xlsxwriter', 'openpyxl']
    install_libs(bucket_name, libraries)

    print("Inserting tmp folder")
    sys.path.insert(0, '/tmp')

    print("importing libraries")
    import pandas as pd
    import xlsxwriter
    import openpyxl

    main_val = get_data_from_body(event)
    print(f"main_val: {main_val}, converting to dataframe...")

    try:
        df = extract_csv_to_dataframe(main_val, pd)
    except Exception as exp:
        return {
            'statusCode': 400,
            'headers': {'Content-Type': 'text/plain'},
            'body': f"Error: {exp}."
        }

    print(f"Shape of df: {df.shape}")

    # Perform EDA and profiling
    results = df.describe()
    print(f"RESULTS: {results}")

    # Create an Excel file
    with io.BytesIO() as output:
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            results.to_excel(writer)
        output_data = output.getvalue()

    print(f"OUTPUT_DATA CHECK: {pd.read_excel(output_data)}")

    # Return the Excel file as a base64-encoded string
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/vnd.openxmlformats-officedocument'
                            '.spreadsheetml.sheet',
            'Content-Disposition': 'attachment; filename=desc_results.xlsx'
        },
        'body': base64.b64encode(output_data).decode('utf-8'),
        'isBase64Encoded': True
    }
