import requests
import threading
import time

# List of URLs
urls = [
    "https://www.google.com",
    "https://www.yahoo.com",
    "https://www.amazon.com",
    "https://www.reddif.com"
]

# -------------------------------
# Function to Download and Save File
# -------------------------------
def download_file(url):
    try:
        # Send HTTP GET request
        response = requests.get(url)
        response.raise_for_status()

        # Extract filename from URL
        filename = url.split("/")[-1] + ".txt"

        # Save content into file
        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"Downloaded: {filename}")

    except Exception as e:
        print(f"Error downloading {url}: {e}")


# ================================
# 1. Sequential Download
# ================================
print("\n--- Sequential Download Started ---")

start_time = time.time()

for url in urls:
    download_file(url)

sequential_time = time.time() - start_time

print(f"\nSequential Download Time: {sequential_time:.2f} seconds")


# 2. Threading Download
print("\n--- Threading Download Started ---")

start_time = time.time()

threads = []

# Create threads for each URL
for url in urls:
    thread = threading.Thread(target=download_file, args=(url,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

threading_time = time.time() - start_time

print(f"\nThreading Download Time: {threading_time:.2f} seconds")



# Final Comparison
print("\n--- Time Comparison ---")
print(f"Sequential Time : {sequential_time:.2f} seconds")
print(f"Threading Time  : {threading_time:.2f} seconds")
