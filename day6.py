import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)

async def main():
    urls = ['https://notepadfromdas.pythonanywhere.com/pad/share']  
    html_pages = await fetch_all(urls)

    all_links = []
    for html in html_pages:
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a') 
        for link in links:
            href = link.get('href')
            if href:  
                all_links.append(href)

    for link in all_links:
        print(link)
        
asyncio.run(main())