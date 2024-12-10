import os
from dotenv import load_dotenv
import google.generativeai as genai
from google.generativeai.types.generation_types import AsyncGenerateContentResponse

from tools import toggle_desk_light_off, toggle_desk_light_on, toggle_lightstrip

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(
    "gemini-1.5-flash",
    tools=[toggle_desk_light_on, toggle_desk_light_off, toggle_lightstrip],
)


async def get_llm_response(text: str) -> AsyncGenerateContentResponse:
    """
    This function is used to get a response from the LLM model.
    """
    prompt = f"""
        You are a helpful assistant that controls the lights in the apartment. I need to track
        state by ON or OFF.
        Example:
        Turn the desk light ON
        Turn the light strip OFF
        If I use this language then return ON or OFF
        {text}
    """
    chat = model.start_chat()
    response = await chat.send_message_async(prompt)

    return response
    # response = await model.generate_content_async(
    #     contents=prompt, tools=[toggle_desk_light, toggle_lightstrip]
    # )
    # return response
