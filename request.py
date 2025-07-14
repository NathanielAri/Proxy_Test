import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("USERNAME1", "").strip()
password = os.getenv("PASSWORD", "").strip()

proxies = {
    "http": f"http://{username}-country-us:{password}@network.joinmassive.com:65535",
    "https": f"https://{username}-country-us:{password}@network.joinmassive.com:65535"
}

for i in range(5):
    try:
        r = requests.get("https://api.ipify.org?format=json", proxies=proxies, timeout=10)
        ip = r.json()["ip"]
        print(f"Request {i + 1}: {ip}")

        geo_response = requests.get(f"https://ipapi.co/{ip}/json/")
        geo = geo_response.json()
        print(f"Country: {geo['country_name']} ({geo['country']})")
    except Exception as e:
        print("Error: ", e)
    
    time.sleep(1)