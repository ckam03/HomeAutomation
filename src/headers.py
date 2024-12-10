import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=(".env"), override=True)

api_key = os.getenv("GOVEE_API_KEY")

govee_headers = {
    "Govee-API-Key": f"{api_key}",
    "Content-Type": "application/json",
}

hue_headers = {
    "hue-application-key": os.getenv("HUE_USERNAME"),
}
