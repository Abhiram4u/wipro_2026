import requests
import threading
import time

urls = [
    "https://www.google.com",
    "https://www.yahoo.com",
    "https://www.amazon.com",
    "https://www.reddif.com"
]

def download_file(url):
    try:
        response = requests.get(url)
        # response.raise_for_status()
        filename = url.split("/")[-1]+".txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Error downloading {url}:{e}")

start_time = time.time()
for url in urls:
    download_file(url)

sequentialtime = time.time() - start_time
print(f"Sequential download time: {sequentialtime}")



threads = []

start_time1 = time.time()
for url in urls:
    thread = threading.Thread(target=download_file, args=(url,))
    threads.append(thread)
    thread.start()

threadingtime = time.time() - start_time1
print(f"Threading download time: {threadingtime}")