from dotenv import load_dotenv

load_dotenv()

from os import getenv

API_ID = getenv("API_ID", "28714959")
API_HASH = getenv("API_HASH", "c0b9797634090ee3f4c1c56db6c051a7"")
BOT_TOKEN = getenv("BOT_TOKEN", "7696841194:AAHMKvyXKZ6BJK8vdUDS4lhxxE6J2jb_uBs")
OWNER_ID = int(getenv("OWNER_ID", "1905251964"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://jiosaavn:jiosaavn@cluster0.ouhhe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
AUTH_CHANNEL = int(getenv("AUTH_CHANNEL", "0"))
FSUB = getenv("FSUB", False)
