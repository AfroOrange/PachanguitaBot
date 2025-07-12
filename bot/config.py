import os
import json
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set in the environment variables.")

# Firebase Configuration
firebase_credentials_str = os.getenv("FIREBASE_CREDENTIALS")
if firebase_credentials_str:
    try:
        FIREBASE_CONFIG = json.loads(firebase_credentials_str)
    except json.JSONDecodeError:
        raise ValueError("FIREBASE_CREDENTIALS is not valid JSON")
else:
    raise ValueError("FIREBASE_CREDENTIALS is not set in the environment variables.")