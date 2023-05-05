import json
from datetime import datetime

def lambda_handler(event, context):
    year = str(datetime.now().year)
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Selpha Google Search</title>
    <style>
        body {{
            background-color: #333;
            font-family: Arial, sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }}
        form {{
            background-color: #222;
            padding: 2rem;
            border-radius: 5px;
        }}
        input[type="text"] {{
            background-color: #555;
            border: none;
            color: white;
            padding: 0.5rem;
            width: 300px;
        }}
        input[type="text"]:focus {{
            outline: none;
            background-color: #666;
        }}
        input[type="submit"] {{
            background-color: #4CAF50;
            color: white;
            padding: 0.5rem 1rem;
            font-size: 1rem;
            border: none;
            cursor: pointer;
            border-radius: 5px;
            margin-left: 0.5rem;
        }}
        input[type="submit"]:hover {{
            background-color: #45A049;
        }}
        .home {{
            position: absolute;
            top: 20px;
            left: 20px;
            background-color: #555;
            color: white;
            padding: 0.5rem 1rem;
            text-decoration: none;
            border-radius: 5px;
            font-size: 1rem;
            transition: background-color 0.2s;
        }}
        .home:hover {{
            background-color: #666;
        }}
        footer {{
            position: absolute;
            bottom: 20px;
            font-size: 0.8rem;
            color: white;
        }}
    </style>
</head>
<body>
    <a class="home" href="https://selpha.com">Home</a>
    <form action="https://www.google.com/search" method="get">
        <input type="text" name="q" placeholder="Search Google...">
        <input type="submit" value="Search">
    </form>
    <footer>
        SelphaWare Solutions &trade; &copy; {year}
    </footer>
</body>
</html>
    """

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html'
        },
        'body': html_content
    }
