import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'TRMB$$4568$$'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Tarek-1488%40ZC@localhost:3306/SMP'
