import sqlite3
import os
from flask import Flask, render_template, request, flash, g, abort
from fdatabase import DataBases


app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'ivask.db')))

DATABASE = '/tmp/ivask.db'
DEBUG = True
SECRET_KEY = 'wehsdjgfhdjkghd493258dhfusdfgfdshj5'


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_request
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route('/')
# @app.route('/index')
def index_page():
    db = get_db()
    dbase = DataBases(db)
    return render_template('index.html', menu=dbase.get_menu(), posts=dbase.get_posts_annonce())
    # return render_template('index.html', title='Iva Skin')

# @app.route('/gotocab')
@app.route('/', methods=['POST', 'GET'])
def add_post():
    db = get_db()
    dbase = DataBases(db)

    if request.method == 'POST':
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.add_post(request.form['name'], request.form['post'])
            if not res:
                flash('Ошибка добавления статьи', category='error')
            else:
                flash('Статья добавлена успешно', category='success')
        else:
            flash('Ошибка добавления статьи', category='error')
    return render_template('index.html', menu=dbase.get_menu())


@app.route('/<int:id_post>')
def show_post(id_post):
    db = get_db()
    dbase = DataBases(db)
    title, post = dbase.get_post(id_post)
    if not title:
        abort(404)
    else:
        return render_template('index.html', menu=dbase.get_menu(), title=title, posts=post)

# @app.errorhandler(404)
# def page_not_found(error):
#     db = get_db()
#     dbase = DataBases(db)
#     return render_template('page404.html',title='Страница не найдена', menu = dbase.get_menu())

if __name__ == '__main__':
    app.run(debug=True)