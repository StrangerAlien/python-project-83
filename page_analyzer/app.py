from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_python_project_83():
    return render_template('index.html')
