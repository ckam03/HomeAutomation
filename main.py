import asyncio, os, argparse
from dotenv import load_dotenv
from govee_client import GoveeClient
from hue_client import HueClient


load_dotenv(dotenv_path=(".env"), override=True)

# Get the environment variables
api_key = os.getenv("GOVEE_API_KEY")
url = os.getenv("GOVEE_URL")
device_control_url = os.getenv("GOVEE_DEVICE_CONTROL")

# Set the headers
govee_headers = {
    "Govee-API-Key": f"{api_key}",
    "Content-Type": "application/json",
}

hue_headers = {
    "hue-application-key": os.getenv("HUE_USERNAME"),
}


async def main():
    parser = argparse.ArgumentParser(description="Govee API controller")
    parser.add_argument(
        "--light_switch", type=str, choices=["on", "off"], help="on or off"
    )
    args = parser.parse_args()

    await on_or_off(args.light_switch)


async def on_or_off(state):
    govee_client = GoveeClient(govee_headers)
    hue_client = HueClient(hue_headers)

    await govee_client.on_or_off(state)
    await hue_client.on_or_off(state)


# Run the main function
asyncio.run(main())
