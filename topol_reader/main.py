import os
import requests

# HA Supervisor poskytuje token přes tuto proměnnou
SUPERVISOR_TOKEN = os.getenv("SUPERVISOR_TOKEN")
HA_API_URL = "http://supervisor/core/api/states/sensor.topol_status"

def read_device_data():
    # Tady simulujeme data – nahradíš vlastním HTTP požadavkem na čističku
    return {"state": "OK", "attributes": {"ph": 7.2, "oxygen": 3.5}}

def send_to_ha(data):
    headers = {
        "Authorization": f"Bearer {SUPERVISOR_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.post(HA_API_URL, headers=headers, json=data)
    print(f"HA response: {response.status_code} {response.text}")

if __name__ == "__main__":
    print("Reading device...")
    device_data = read_device_data()
    send_to_ha(device_data)
