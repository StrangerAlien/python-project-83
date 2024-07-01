from flask import Flask, render_template, request, flash, redirect, url_for
from page_analyzer.secrets import SECRET_KEY
from page_analyzer import actions_with_db as db

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def index():
    return render_template('index.html', url='')


@app.get('/urls')
def get_all_urls():
    with db.connect_db():
        url_data = db.get_data_all_urls()
        return render_template('urls.html', urls=url_data)


@app.post('/urls')
def post_urls():
    data = request.form.to_dict()
    url = data.get('url').lower()

    url_id = db.save_url(url)
    return redirect(url_for('get_url', url_id=url_id))


@app.get('/urls/<int:url_id>')
def get_url(url_id):
    with db.connect_db():
        url_data = db.get_data_by_id(url_id)

        name = url_data[1]
        date = url_data[2]

    return render_template('url.html', url_id=url_id, name=name, date=date)


# @app.post('/urls/<int:url_id>/checks')
# def post_url():
#     data = request.form.to_dict()
#     url = data.get('url').lower()
#
#     db.save_url(url)
#     return render_template('index.html')
