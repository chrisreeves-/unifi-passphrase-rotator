import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

ip = input("Please enter the Unifi controllers ip address: ")
port = input("Please enter the Unifi controllers port numnber: ")
username = input("Please enter your username to access the Unifi controller: ")
password = input("Please enter your password to access the Unifi controller: ")
SSID = input("Please enter the SSID you want to rotate: ")

# Remove unverified HTTPS request warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Auth Headers
headers = {"Accept": "application/json",
           "Content-Type": "application/json"}
controller = f"https://{ip}:{port}/api/login"
body = {
    "username": f"{username}",
    "password": f"{password}"
}

# Auth to Unifi Controller
session = requests.Session()
response = session.post(controller, headers=headers, data=json.dumps(body), verify=False)
api_data = response.json()

# Set Sites
url = f"https://{ip}:{port}/api/self/sites"
response = session.get(url, headers=headers, verify=False)
api_data = response.json()
for name in api_data["data"]:
    sitename = (name["name"])

# Get Config
url = f"https://{ip}:{port}/api/s/{sitename}/rest/wlanconf"
response = session.get(url, headers=headers, verify=False)
api_data = response.json()
