import requests
from bs4 import BeautifulSoup
import json

url = "https://www.w3schools.com/html/html_tables.asp"


response = requests.get(url)
response.raise_for_status()


soup = BeautifulSoup(response.text, "html.parser")


pagetitle = soup.title.string.strip() if soup.title else "No title"
print("Page Title:", pagetitle)


links = soup.find_all("a")
links_list = []

for link in links:
    href = link.get("href")
    if href:
        links_list.append(href)

print("Total Links Found:", len(links_list))


tabledata = []
table = soup.find("table", {"id": "customers"})

if table:
    rows = table.find_all("tr")[1:]  # Skip header row
    for row in rows:
        columns = row.find_all("td")
        row_data = {
            "company": columns[0].text.strip(),
            "contact": columns[1].text.strip(),
            "country": columns[2].text.strip()
        }
        tabledata.append(row_data)


extracted_data = {
    "page_title": pagetitle,
    "total_links": len(links_list),
    "links": links_list,
    "table_data": tabledata
}


with open("extracted_data.json", "w", encoding="utf-8") as file:
    json.dump(extracted_data, file, indent=4)

print("Data successfully saved to extracted_data.json")
