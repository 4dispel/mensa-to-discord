import json
import requests
from datetime import datetime

def send_message(webhook_url, message):
    if type(message) != type("string"):
        message = str(message)
    requests.post(webhook_url, json={'content': message}, params={"wait": True})

def http_request(url):
    return requests.get(url)


def get_canteen_link():
    current_date = datetime.now().strftime('%Y-%m-%d')
    return f"https://openmensa.org//api/v2/canteens/79/days/{current_date}/meals"

def extract_json(x):
    return x.json()

def generate_message(data):
    msg = f"alte mensa menü {datetime.now().strftime(r'%d.%m.%Y')} :\n"
    for i in data:
        msg += i['name']
        msg += "\n"
        msg += str(i['prices']['students'])
        msg += "€\n"
    return msg

def main():
    webhook_url = "" #your webhook url(from the integration menu in server settings)
    url = get_canteen_link()
    response = http_request(url)
    data = extract_json(response)
    message = generate_message(data)
    send_message(webhook_url, message)
    
if __name__ == "__main__":
    main()