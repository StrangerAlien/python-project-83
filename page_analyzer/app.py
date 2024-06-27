from flask import Flask, render_template, request
from page_analyzer.secrets import SECRET_KEY
from page_analyzer import actions_with_db as db

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def index():
    return render_template('index.html', url='')


@app.post('/urls')
def post_urls():
    data = request.form.to_dict()
    url = data.get('url').lower()

    db.save_url(url)
    return render_template('inside_base.html')


@app.get('/urls')
def get_urls():
    pass
