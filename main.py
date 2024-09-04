import httpx, asyncio, os, argparse
from dotenv import load_dotenv
from govee_client import GoveeClient


load_dotenv(dotenv_path=(".env"), override=True)

# Get the environment variables
api_key = os.getenv("GOVEE_API_KEY")
url = os.getenv("GOVEE_URL")
device_control_url = os.getenv("GOVEE_DEVICE_CONTROL")

headers = {
    "Govee-API-Key": f"{api_key}",
    "Content-Type": "application/json",
}


async def main():
    parser = argparse.ArgumentParser(description="Govee API controller")
    parser.add_argument(
        "--state", type=str, choices=["OFF", "ON"], help="0 for off, 1 for on"
    )
    args = parser.parse_args()

    govee_client = GoveeClient(headers)
    # check if args.state is null
    await govee_client.on_or_off(args.state)


# Run the main function
asyncio.run(main())
