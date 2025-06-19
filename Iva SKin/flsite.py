from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
# @app.route('/index')
def index_page():
    return render_template('index.html', title='Iva Skin')


if __name__ == '__main__':
    app.run(debug=True)
