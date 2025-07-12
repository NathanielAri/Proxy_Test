import requests
import time

proxies = {
    "http": "http://mpuSMHbGJM:JoIawiGZ1UUxhO21dv3n@network.joinmassive.com:65535",
    "https": "https://mpuSMHbGJM:JoIawiGZ1UUxhO21dv3n@network.joinmassive.com:65535"
}

for i in range(5):
    try:
        r = requests.get("https://api.ipify.org?format=json", proxies=proxies, timeout=10)
        print(f"Request {i + 1}: ", r.json()["ip"])
    except Exception as e:
        print("Error: ", e)
    
    time.sleep(1)