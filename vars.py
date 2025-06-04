# DON'T add anything here just add in render's secret or env section 
from os import environ

API_ID = int(environ.get("API_ID", "27536109"))
API_HASH = environ.get("API_HASH", "b84d7d4dfa33904d36b85e1ead16bd63")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
