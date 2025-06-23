from flask import Flask, render_template, g
import sqlite3
import os
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
    return render_template('index.html', menu=dbase.get_menu())
    # return render_template('index.html', title='Iva Skin')

# @app.route('/gotocab')


if __name__ == '__main__':
    app.run(debug=True)
