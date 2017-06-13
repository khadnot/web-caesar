from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)

app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sand-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin:10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="post">
            <label>Rotate by:
            <input type="text" name="rot" value="0"/>
            </label>
            <textarea type="text" name="text">{0}</textarea>
            <br>
            <input type="submit" />
        </form>
    </body>
</html>
"""

@app.route('/', methods=['POST'])
def encrypt():
    text = request.form['text']
    rot = int(request.form['rot'])
    new_text = rotate_string(text, rot)
    return "<h1>" + form.format(new_text) + "</h1>"

@app.route("/")
def index():
    return form.format('')
    return encrypt(text, rot)

app.run()
