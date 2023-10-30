import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "22377432").strip()
API_HASH = os.getenv("API_HASH", "69dbb3a23605d52444caf76c39631dd6").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "6362933544:AAE4S_QQ5KnOJgkxD1DHme2Yc0He0CVvE_g").strip()
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ilxnvuj833:0212@cluster0.ile0pdo.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = os.getenv("OWNER_ID", "1839010591")
MUST_JOIN = os.getenv("MUST_JOIN", "amwangs")

if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")
'''
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit
'''

try:
    API_ID = int(API_ID)
except ValueError:
    raise SystemExit("API_ID is not a valid integer. Exiting...")
