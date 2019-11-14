from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists


app = Flask(__name__)
app.config.from_object('config.Config')

csrf = CSRFProtect(app)
db = SQLAlchemy(app)

if not database_exists('sqlite:////tmp/test.db'):
    db.create_all()

import views

if __name__ == "__main__":
    app.run()