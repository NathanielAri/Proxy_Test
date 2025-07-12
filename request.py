import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("USERNAME1", "").strip()
password = os.getenv("PASSWORD", "").strip()

proxies = {
    "http": f"http://{username}:{password}@network.joinmassive.com:65535",
    "https": f"https://{username}:{password}@network.joinmassive.com:65535"
}

for i in range(5):
    try:
        r = requests.get("https://api.ipify.org?format=json", proxies=proxies, timeout=10)
        print(f"Request {i + 1}: ", r.json()["ip"])
    except Exception as e:
        print("Error: ", e)
    
    time.sleep(1)