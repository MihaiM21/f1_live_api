# import asyncio
# import websockets
# import json
#
# live_data = {}
#
# async def collect_data():
#     uri = "wss://livetiming.formula1.com/some_endpoint"
#     async with websockets.connect(uri) as ws:
#         while True:
#             msg = await ws.recv()
#             data = json.loads(msg)
#             # Update local state
#             live_data["timestamp"] = data.get("time")
#             live_data["positions"] = data.get("drivers", {})
#
# print(live_data)

# main.py
import requests

url = "https://livetiming.formula1.com/static/2024/2024-05-05_Miami_Race/SessionInfo.json"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Referer": "https://livetiming.formula1.com/",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Success:", response.json())
else:
    print(f"Failed: {response.status_code}")
