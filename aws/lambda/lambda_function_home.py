def lambda_handler(event, context):
    """
    Selphaware home page
    :param event:
    :param context:
    :return:
    """
    body = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SelphaWare Solutions</title>
    <style>
        body {
            background-color: #333;
            font-family: Arial, sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            flex-direction: column;
            margin: 0;
            color: #fff;
        }

        h1 {
            font-size: 3em;
            font-weight: bold;
            margin-bottom: 20px;
        }

        h2 {
            font-size: 1.2em;
            font-weight: lighter;
        }

        a {
            color: #4a90e2;
            text-decoration: none;
            font-weight: 400;
        }

        a:hover {
            text-decoration: underline;
        }

        footer {
            position: fixed;
            bottom: 20px;
            width: 100%;
            color: #777;
            text-align: center;
        }
    </style>
</head>
<body>
    <div>
        <h1>SelphaWare Solutions</h1>
        <h2>&copy; 2023 SelphaWare Solutions&trade;</h2>
        <a href="https://selpha.com/desc">selpha.com/desc</a><br>
        <a href="https://selpha.com/eda">selpha.com/eda</a><br>
        <a href="https://selpha.com/google">selpha.com/google</a>
    </div>
    <footer>
        <p>&copy; 2023 SelphaWare Solutions&trade;. All rights reserved. <br>Sana 
        | Shayaan | Zuhaib | Mikaeel </p>
    </footer>
</body>
</html>
"""

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html'
        },
        'body': body
    }
