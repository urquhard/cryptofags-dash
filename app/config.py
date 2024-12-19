import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "default_secret")
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")
    DATA_FILE_1 = os.environ.get("DATA_FILE_1")
    DATA_FILE_2 = os.environ.get("DATA_FILE_2")
