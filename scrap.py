import requests
from bs4 import BeautifulSoup
import csv

# Membuat permintaan HTTP
url = "https://www.bbc.co.uk/news"
response = requests.get(url)

if response.status_code == 200:
    content = response.text

    # Mem-parsing konten halaman web
    soup = BeautifulSoup(content, "html.parser")

    # Mencari elemen dengan kelas yang sesuai untuk judul berita
    news_headlines = soup.find_all("h3", class_="gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text")
    news_headlines = soup.find_all("h3", class_="gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text")
    
    # Menyimpan judul-judul berita dalam format CSV
    with open("bbc_news_headlines.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Judul Berita"])

        for headline in news_headlines:
            writer.writerow([headline.text.strip()])

    print("Data telah disimpan dalam format CSV.")
else:
    print("Permintaan gagal")
