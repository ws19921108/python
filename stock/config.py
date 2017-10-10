#-*-coding:utf-8-*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# email server
MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'ws19921108'
MAIL_PASSWORD = '*********'

# administrator list
ADMINS = ['ws19921108@163.com']


