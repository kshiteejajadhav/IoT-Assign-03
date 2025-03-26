import requests
import json
from datetime import datetime, timedelta

CHANNEL_ID = "2894190"
READ_API_KEY = "ECX3SBNSRANIG0HG"

def get_5hrs_data():
    url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}&results=1000"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        return

    data = response.json()
    feeds = data.get("feeds", [])
    if not feeds:
        print("No feeds found.")
        return

    # Define the time threshold (5 hours ago from now in UTC)
    now = datetime.utcnow()
    cutoff = now - timedelta(hours=5)
    
    print("=== Sensor Data from the Last 5 Hours ===")
    for feed in feeds:
        created_str = feed.get("created_at")
        if created_str:
            created_dt = datetime.strptime(created_str, "%Y-%m-%dT%H:%M:%SZ")
            if created_dt >= cutoff:
                print(f"Time: {created_dt}")
                print(f"  Temperature: {feed.get('field1')}")
                print(f"  Humidity: {feed.get('field2')}")
                print(f"  CO2: {feed.get('field3')}")
                print("------------")

if __name__ == "__main__":
    get_5hrs_data()
