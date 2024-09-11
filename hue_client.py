import httpx, os


class HueClient:
    def __init__(self, headers) -> None:
        self.headers = headers

    async def on_or_off(self, state: bool):

        light_state = True if state == "on" else False
        api_request = {"on": {"on": light_state}}

        async with httpx.AsyncClient(verify=False) as client:
            response = await client.put(
                url=os.getenv("HUE_URL"),
                headers=self.headers,
                json=api_request,
            )
            return response.json()
