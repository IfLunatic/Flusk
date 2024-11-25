import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'asdczxcasdasdasdadazxc')  
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1111@localhost/library'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'asdjbnzhxjczxcjhzjxhcb')  
