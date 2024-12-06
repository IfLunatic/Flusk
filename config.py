import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'asdczxcasdasdasdadazxc')  
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://avnadmin:AVNS_-FBHwDlqhNmixCAfWuQ@pg-2e343b22-dimazedofficial-1778.e.aivencloud.com:15983/defaultdb"
        "?sslmode=require&sslrootcert=path/to/ca.pem"  
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'asdjbnzhxjczxcjhzjxhcb')  
