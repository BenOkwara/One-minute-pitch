import os

class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:dtbase@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = 'True'
    @staticmethod
    def init_app(app):
        pass

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}
