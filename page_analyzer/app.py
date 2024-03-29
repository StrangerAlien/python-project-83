from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_python_project_83():
    return 'Welcome to python project 83'
