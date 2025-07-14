# Proxy_Test
This program tests a proxy at certain URLs. You can change the proxies to test by replacing the URLs that is entered in proxies.

## Requirements
* Python Request library installed
* Python load_dotenv library installed (If using a .env file)

## Getting Started
1. Clone the Github
```bash
git clone https://github.com/NathanielAri/Proxy_Test.git
cd Proxy_Test
```
2. Change proxies (if you want to test different proxy)

3. Create a .env file
```bash
vim .env.local
```
or
```bash
touch .env.local
```

Then add your username and password to .env.local
```bash
USERNAME1="YOUR_USERNAME_HERE"
PASSWORD="PASSWORD_HERE"
```

4. To test run the following:
```bash
python/python3 requests.py
```