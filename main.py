from flask import Flask

app = flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sand-serif;
                border-radius: 10px;
            }
            textarea {
                margin:10px;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
    <!-- create form here....-->
    </body>
</html>

@app.route('/')
def index():
    return 'Hello World'

app.run()
