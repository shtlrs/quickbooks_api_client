from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_VERSION = 3
MINOR_VERSION = 62
REALM_ID = getenv("REALM_ID", None)
BASE_URL = f"https://quickbooks.api.intuit.com/{API_VERSION}/company/{REALM_ID}/"
