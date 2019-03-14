import os
import ssl

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG=True

    #Mongoengine Variables
    MONGODB_SETTINGS={
        'host': os.environ.get('MONGODB_HOST'), 
        #below two are needed if `+srv` in uri like for Mongo Atlas
        'ssl': True, 
        'ssl_cert_reqs': ssl.CERT_NONE
    }
    
    #REDDIT API
    REDDIT_ID='m5Q5N6H9lFZ-qw'
    REDDIT_SECRET='71pM2Gcqcr0QdbycdusmATGs7TI'
    REDDIT_REDIRECT_URI='http://127.0.0.1:5000/'
    REDDIT_USER_AGENT='android:mysignal:v0.1 (by /u/yourcousinbob)'

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
