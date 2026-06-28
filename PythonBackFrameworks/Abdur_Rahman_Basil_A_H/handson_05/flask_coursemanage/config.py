import os

class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-default-key'
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///coursemanager.db'
    
    DEBUG = True