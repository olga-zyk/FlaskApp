from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from database.models import *


app = Flask(__name__)


def create_app():
    Bootstrap(app)
    with app.app_context():
        db.init_app(app)

    return app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
