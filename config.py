import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, os.getenv('DATABASE_NAME'))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI =  f'sqlite:///{db_path}'