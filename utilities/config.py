from dotenv import load_dotenv
import os
from pathlib import Path

# Load from .env file
# env_path = Path(__file__).resolve().parent.parent / ".env"
# load_dotenv(dotenv_path=env_path)


# env_name = os.getenv("ENV", "development") 
# load_dotenv(dotenv_path=f"../.env.{env_name}")

env_path = Path(__file__).resolve().parents[2] / ".env.development"
load_dotenv(dotenv_path=env_path)


class Settings:
    PROFILE_UPLOAD_FOLDER = os.getenv("PROFILE_UPLOAD_FOLDER")
    OWNER_PORTAL_URL = os.getenv("OWNER_PORTAL_URL")
    OWNER_PORTAL_URL_LOCAL = os.getenv("OWNER_PORTAL_URL_LOCAL")
    SECRET_KEY = os.getenv("SECRET_KEY")
    HOSTELVALLEY_DB_URL = os.getenv("HOSTELVALLEY_DB_URL")

    def __init__(self):
        self.PROFILE_UPLOAD_FOLDER = os.getenv("PROFILE_UPLOAD_FOLDER")
        self.OWNER_PORTAL_URL = os.getenv("OWNER_PORTAL_URL")
        self.OWNER_PORTAL_URL_LOCAL = os.getenv("OWNER_PORTAL_URL_LOCAL")
        self.SECRET_KEY = os.getenv("SECRET_KEY")
        self.HOSTELVALLEY_DB_URL = os.getenv("HOSTELVALLEY_DB_URL")
        print(f"OWNER_PORTAL_URL_LOCAL: {self.OWNER_PORTAL_URL_LOCAL}")

settings = Settings()
print(f"Settings: {settings}")