import requests
import json
import time
import random

SERVER_URL = 'http://127.0.0.1:5000/logs'
TOKEN = 'service2_token'

def generate_logs():
    while True:
        log_data = {
            "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S'),
            "service_name": "service1",
            "severity": random.choice(["INFO", "ERROR", "DEBUG"]),
            "message": "Mensaje log desde el servicio 1"
        }
        headers = {
            "Authorization": TOKEN,
            "Content-Type": "application/json"
        }
        response = requests.post(SERVER_URL, headers=headers, data=json.dumps(log_data))
        print(f"Service 1 log sent, status: {response.status_code}")
        time.sleep(random.randint(1, 5))

if __name__ == "__main__":
    generate_logs()
