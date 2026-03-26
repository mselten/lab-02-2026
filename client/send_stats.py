import psutil
import requests
import time

SERVER_URL = "http://localhost:80/stats"


def send_stats():
    cpu = psutil.cpu_percent(interval=None)
    ram = psutil.virtual_memory().percent

    try:
        requests.post(SERVER_URL, json={"cpu": cpu, "ram": ram}, timeout=1)
    except requests.exceptions.RequestException as e:
        print(f"Error sending stats: {e}")


def main():
    print("Client started. Sending stats to server...")
    print(f"Server URL: {SERVER_URL}")

    while True:
        send_stats()
        time.sleep(1)


if __name__ == "__main__":
    main()
