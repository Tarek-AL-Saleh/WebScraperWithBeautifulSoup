# Web Scraper with BeautifulSoup

# Project Description
This project uses Python and BeautifulSoup to scrape book data (titles, links, prices, availability) from a static HTML site into an .csv output file, demonstrating basic web scraping techniques.

# Website Chosen
[http://books.toscrape.com]
This was chosen for its clean HTML structure and static content, and low complexity of the elements.

# How to Use
- have Python 3 or above
- install beautifulsoup4 library
- run the script: python scraper.py
- check the output.csv file for the data

# Observations
- the url used in elements were relative urls, so I had to concatenate them with the website url to get the full link.
- I had to find the common class names between all book cards to be able to extract the data.
- The price had some weird symbols when scaped, so I had to clean it by simply modifying the string.