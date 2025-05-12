
#Question-8:
'''Given a URL, download that and parse 
and download all links inside that page 
    Use ThreadPoolExecutor or ProcessPoolExecutor 
    BeautifulSoup for parsing html, requests for downloading'''
 

import os
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

class WebScraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_and_save(self, url):
        try:
            response = requests.get(url, timeout=10)
            filename = url.replace('http://', '').replace('https://', '').replace('/', '_') + ".html"
            with open(filename, 'w') as file:
                file.write(response.text)
            print(f"Saved {url}")
        except Exception as e:
            print(f"Failed to fetch {url}: {e}")

    def scrape(self):
        main_page_html = requests.get(self.base_url, timeout=10).text
        soup = BeautifulSoup(main_page_html, 'html.parser')
        links = [tag['href'] for tag in soup.find_all('a', href=True) if tag['href'].startswith('http')]
        with ThreadPoolExecutor() as executor:
            executor.map(self.fetch_and_save, links)

if __name__ == "__main__":
    scraper = WebScraper("https://notepadfromdas.pythonanywhere.com/pad/share")
    scraper.scrape()
