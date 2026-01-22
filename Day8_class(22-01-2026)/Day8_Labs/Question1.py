# Write a Python program that:
#
# 1.Uses the requests library to send a GET request to a public REST API(e.g., users or posts API)
#
# 2. Sends custom headers with the request
#
# 3. Parses the JSON response and extracts specific fields
#
# 4. Serializes the extracted data and saves it into a JSON file
#
# 5. Handles HTTP errors using proper exception handling
#


import requests
import json

url = "http://127.0.0.1:5000/details"

headers = {
    "User-Agent": "Python-Requests-Demo",
    "Accept": "application/json"
}

try:

    response = requests.get(url, headers=headers,timeout=5)

    response.raise_for_status()

    details = response.json()

    extracted_data = []
    for user in details:
        extracted_data.append({
            "id": user["id"],
            "name": user["name"],
            "email": user["email"]

        })

    with open("details_data.json","w") as f:
        json.dump(extracted_data,f,indent=4)

    print("Data successfully uploaded to users_data.json")
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")

except requests.exceptions.ConnectionError:
    print("Error: Unable to connect to the server")

except requests.exceptions.Timeout:
    print("Error: Request timed out")

except requests.exceptions.RequestException as err:
    print(f"Unexpected error: {err}")

