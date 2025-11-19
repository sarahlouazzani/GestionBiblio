import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://sarah:sarah123@localhost:5432/gestionbiblio"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
