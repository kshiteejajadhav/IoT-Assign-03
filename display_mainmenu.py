import requests
import json
from datetime import datetime, timedelta

CHANNEL_ID = "2894190"
READ_API_KEY = "ECX3SBNSRANIG0HG"

def get_latest_data():
    url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds/last.json?api_key={READ_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("=== Latest Data from ThingSpeak ===")
        print(f"Entry ID: {data.get('entry_id')}")
        print(f"Temperature: {data.get('field1')}")
        print(f"Humidity: {data.get('field2')}")
        print(f"CO2: {data.get('field3')}")
        print(f"Created at: {data.get('created_at')}")
    else:
        print(f"Error fetching data: {response.status_code}")

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

    now = datetime.utcnow()
    cutoff = now - timedelta(hours=5)
    
    print("=== Sensor Data from the Last 5 Hours ===")
    for feed in feeds:
        created_str = feed.get("created_at")
        if created_str:
            created_dt = datetime.strptime(created_str, "%Y-%m-%dT%H:%M:%SZ")
            if created_dt >= cutoff:
                print(f"Time: {created_dt} -> Temperature: {feed.get('field1')}, Humidity: {feed.get('field2')}, CO2: {feed.get('field3')}")

def main():
    while True:
        print("\nSelect an option:")
        print("1. Display latest sensor data")
        print("2. Display sensor data from the last 5 hours")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            get_latest_data()
        elif choice == "2":
            get_5hrs_data()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
