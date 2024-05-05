# config.py

import os

class Config:
    SECRET_KEY = '$$TRMB$$'  # Consider using os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://trmb:$$BASMOTESH123@reunion.mysql.database.azure.com/reunion'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
