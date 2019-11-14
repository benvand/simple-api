class Config:
    DEBUG = True
    FLASK_ENV = 'development'
    SECRET_KEY = 'test'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True