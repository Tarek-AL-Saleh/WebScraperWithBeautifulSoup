import requests
import html
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "URL", "Price", "Availability"])
    books = soup.select('article.product_pod')
    for book in books:
        title = book.h3.a['title']
        link = book.h3.a['href']
        full_link = url + link
        price = book.select_one('.price_color').text
        availability = book.select_one('.availability').text.strip()
        writer.writerow([title, full_link, price[1:], availability])
print("Data saved to output.csv")
