from bs4 import BeautifulSoup

with open("patient_list.html") as file:
    soup = BeautifulSoup(file, "html.parser")

rows = soup.find_all("tr")[1:]

for row in rows:
    cols = row.find_all("td")
    print(
        cols[0].text,
        cols[1].text,
        cols[2].text,
        cols[3].text
    )
