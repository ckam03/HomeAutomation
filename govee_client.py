import os, uuid, httpx

from device_state import DeviceState


class GoveeClient:
    def __init__(self, headers) -> None:
        self.headers = headers

    async def on_or_off(self, state: str):
        on_or_off = DeviceState[state]
        request_id = str(uuid.uuid4())

        api_request = {
            "requestId": request_id,
            "payload": {
                "sku": os.getenv("GOVEE_DEVICE_SKU"),
                "device": os.getenv("GOVEE_DEVICE_ID"),
                "capability": {
                    "type": "devices.capabilities.on_off",
                    "instance": "powerSwitch",
                    "value": on_or_off.value,  # 0 for off, 1 for on
                },
            },
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                os.getenv("GOVEE_DEVICE_CONTROL"),
                headers=self.headers,
                json=api_request,
            )
            return response.json()
