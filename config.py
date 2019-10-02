import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "ahrUr.bA@c-QfF7ZNWK*"
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.mailgun.org')
    # MAIL_DEFAULT_SENDER = 'Conscious Psychology<noreply@burgercraft.org>'
    # MAIL_PASSWORD = '1318cd4cfd3977951446f2fdaa2b8322-4a62b8e8-b5ac6f25'
    # MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    # MAIL_USERNAME = 'postmaster@mg.burgercraft.org'
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
    #                ['true', 'on', '1']
    # SITE_ADMIN = os.environ.get("SITE_ADMIN") or 'joelkells@protonmail.com'
    # POSTS_PER_PAGE = 10

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}