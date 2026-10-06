import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://feb.ugm.ac.id/en/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Ambil judul berita (h3 yang linknya mengandung /news/)
titles = soup.find_all("h3")
data_berita = []
for item in titles:
    a = item.find("a")
    if a and "/news/" in a.get("href", ""):
        data_berita.append({"judul": a.get_text(strip=True), "link": a["href"]})

# Ambil semua link
links = soup.find_all("a")
data_link = []
for item in links:
    teks = item.get_text(strip=True)
    href = item.get("href")
    if teks and href:
        data_link.append({"teks": teks, "link": href})

# Yang di-print
print("Status code :", response.status_code)
print("Title       :", soup.title.get_text(strip=True))
print("Jumlah berita:", len(data_berita))

# Simpan ke CSV
pd.DataFrame(data_berita).to_csv("febugm_berita.csv", index=False)
pd.DataFrame(data_link).to_csv("febugm_link.csv", index=False)