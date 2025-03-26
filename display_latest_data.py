import requests
import json

CHANNEL_ID = "2894190"
READ_API_KEY = "ECX3SBNSRANIG0HG" 

def get_latest_data():
    url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds/last.json?api_key={READ_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("=== Latest Data from ThingSpeak ===")
        print(f"Entry ID: {data.get('entry_id')}")
        print(f"Temperature (field1): {data.get('field1')}")
        print(f"Humidity (field2): {data.get('field2')}")
        print(f"CO2 (field3): {data.get('field3')}")
        print(f"Created at: {data.get('created_at')}")
    else:
        print(f"Error fetching data: {response.status_code}")

if __name__ == "__main__":
    get_latest_data()
