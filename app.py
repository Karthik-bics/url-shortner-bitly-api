from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()

headers = {
        'Authorization': f"Bearer {os.getenv('BITLY_ACCESS_TOKEN', '')}"
    }

def get_groups():
    API_URL="https://api-ssl.bitly.com/v4/groups"
    response = requests.get(url=API_URL, headers=headers)
    if response.status_code ==200:
        print(response.json())

def generate_short_url(url:str) -> str:
    API_URL = 'https://api-ssl.bitly.com/v4/shorten'
   
    data = json.dumps({
        "group_guid": "Bo724WHxuLJ",
        "domain": "bit.ly",
        "long_url": url
    })
    print(data)
    headers["Content-Type"] = "application/json"
    response = requests.post(url=API_URL, data=data, headers=headers)
    if(response.status_code == 200):
        response_json = response.json()
        print(response_json)
        return "success"
    else:
        print(response.text)


if __name__ == "__main__":
    url = input("Please enter your url\n")
    if url:
        generate_short_url(url)
    
