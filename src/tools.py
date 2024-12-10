import os
from dotenv import load_dotenv
from govee_client import GoveeClient
from hue_client import HueClient
import google.generativeai as genai
import headers

load_dotenv()


async def toggle_desk_light_on(state: str) -> dict:
    """This function is used to toggle the desk light on.
    Args:
        state (str): The state of the light (on)

    Returns:
        the reponse from the API
    """
    print(f"Toggling desk light: {state}")
    govee_client = GoveeClient(headers.govee_headers)
    return await govee_client.on_or_off("on")


async def toggle_desk_light_off(state: str) -> dict:
    """This function is used to toggle the desk light off.
    Args:
        state (str): The state of the light (off)

    Returns:
        the reponse from the API
    """
    print(f"Toggling desk light: {state}")
    govee_client = GoveeClient(headers.govee_headers)
    return await govee_client.on_or_off("off")


async def toggle_lightstrip(state: str) -> dict:
    """
    This function is used to toggle the lightstrip on or off.
    """
    print("Toggling lightstrip")
    hue_client = HueClient()
    return await hue_client.on_or_off(state)
