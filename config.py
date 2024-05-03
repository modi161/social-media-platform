# config.py

import os

class Config:
    SECRET_KEY = '$$TRMB$$'  # Consider using os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Tarek-1488%40ZC@localhost/reunion'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
