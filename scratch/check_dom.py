import urllib.request
import json
import re

req = urllib.request.Request(
    "http://127.0.0.1:7860/api/predict",
    data=json.dumps({"data": ["hello", []], "event_data": None, "fn_index": 0, "session_hash": "test"}).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)

try:
    with urllib.request.urlopen(req) as response:
        print(response.read().decode())
except Exception as e:
    print("API not responding", e)
