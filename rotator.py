import http.client
import random
import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

ip = input("Please enter the Unifi controllers ip address: ")
username = input("Please enter your username to access the Unifi controller: ")
password = input("Please enter your password to access the Unifi controller: ")
SSID = input("Please enter the SSID you want to rotate: ")

# Remove unverified HTTPS request warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def unifi_auth():
    headers = {"Accept": "application/json",
               "Content-Type": "application/json"}
    controller = f"https://{ip}:8443/api/login"
    body = {
        "username": f"{username}",
        "password": f"{password}"
    }
    session = requests.Session()
    response = session.post(controller, headers=headers, data=json.dumps(body), verify=False)
    api_data = response.json()
    print(api_data)

def unifi_wireless_config():
    print("hello world")

def unifi_phrase_rotate():
    print("hello world")

def main():
    print("do a thing")