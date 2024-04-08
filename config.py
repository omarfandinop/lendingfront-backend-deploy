import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    PORT = int(os.getenv("PORT", 5000))
    DEBUG = os.getenv("DEBUG", "False").lower() in ["true", "1"]
    REFERENCE_VALUE = int(os.getenv("REFERENCE_VALUE", 50000))
