from flask import Flask, render_template
from database.models import *


app = Flask(__name__)


def create_app():
    with app.app_context():
        db.init_app(app)

    return app


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app = create_app()
    app.run()
