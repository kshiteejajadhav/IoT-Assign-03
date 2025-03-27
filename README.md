**IoT_Assign_03**

This repository contains the implementation for Assignment 3 of CIS600: IoT Application Development (Spring 2025). 
The goal is to simulate environmental sensor data and publish it to ThingSpeak using the MQTT protocol. 
Along with it, scripts to read and analyze the measurements with ThingSpeak's API are included.

**Project Structure**
* thinkspeak_mqtt_KJ.py          : Simulates and publishes data to ThingSpeak (MQTT)
* display_latest_data.py         : Fetches and displays the most recent data entry
* display_5hrs_data.py           : Fetches all entries from the past 5 hours
* display_mainmenu.py            : Simple menu interface to navigate data display options
* README                         : Project documentation (this file)

**Dependencies**
(Ensure you install these Python packages)
* paho-mqtt
* requests

**Install using pip:**
* pip install paho-mqtt requests

**Environment:**
* Python 3.7 and above
* macOS, Linux, or Windows (tested on macOS using Anaconda)

**Setup**
* Thingspeak account is created on thingspeak.com
* New channel creation with Field1 as Temperature, Field2 as Humidity, Field3 as CO2
* MQTT Device added to channel and save the following:
	1) MQTT Client ID
	2) MQTT Username
	3) MQTT Password
* Authorize the device to publish to your created channel
* Note Channel ID and Read API Key

**How to Run**

	 To publish simulated data to ThingSpeak:
		python3 thinkspeak_mqtt_KJ.py
	
	 To display the latest data entry from ThingSpeak:
		python3 display_latest_data.py
	
	 To display all the data entries from the last 5 hours:
		python3 display_5hrs_data.py
	
	 To display options using an interactive menu:
		python3 display_mainmenu.py

**Checklist Before Submission**
* Provided fields in ThingSpeak channel are appropriately named as field1, field2, and field3
* MQTT credentials for devices are as in the Python script
* MQTT Topic: Well-formed as channels/channel_id/publish
* Correct Read API Key provided to retrieve data in the reading scripts
* Validated scripts with testing to give proper data
* Data shows in the graph on ThingSpeak private view

**Learnings**
* Got practical experience sending MQTT data from Python to ThingSpeak
* Used ThingSpeak REST APIs to retrieve and analyze time-series data
* Understood simulating, parsing, and visualizing environmental data
* Practiced debugging network communication and validation of API responses

**Screenshots to Submit**
* Terminal output from thinkspeak_mqtt_KJ.py
* Terminal output from display_latest_data.py and display_5hrs_data.py
* ThingSpeak graphs of real-time data
* Screenshot of the MQTT device setup and active connection
