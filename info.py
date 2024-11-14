import re
from os import environ, getenv

API_ID = environ.get("API_ID", "28714959")
API_HASH = environ.get("API_HASH", "c0b9797634090ee3f4c1c56db6c051a7")
BOT_TOKEN = environ.get("BOT_TOKEN", "7696841194:AAHMKvyXKZ6BJK8vdUDS4lhxxE6J2jb_uBs")
OWNER_ID = int(environ.get("OWNER_ID", "1905251964"))
MONGO_URL = environ.get("MONGO_URL", "mongodb+srv://jiosaavn:jiosaavn@cluster0.ouhhe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002076230596"))
FSUB = environ.get("FSUB", False)
