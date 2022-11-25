import requests
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from databaseModules import database
  
def getUrls():
    baseUrl = "http://fanfox.net/manga/"
    database.init_database()
    titles = database.retrieve_data()
    formatTitle = lambda title : title.casefold().replace(" ", "_").replace(":", "").replace("!", "").replace("?", "").replace("'", "_").replace("(","").replace(")","").replace(",","").replace(".","").replace("-","_")
    return [baseUrl+formatTitle(title) for title in titles]

async def getPage(session,url):
    async with session.get(url) as response:
        return await response.text()

async def getAllPages(session,urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(getPage(session,url))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results    

async def main(urls):
    async with aiohttp.ClientSession() as session:
        data = await getAllPages(session,urls)
        return data

def scrape(data):
    newBooks_Dates = {}
    for html in data:
        soup = BeautifulSoup(html, 'html.parser')
        results =  soup.find("img",class_="new-pic")
        if results != None:
            title = soup.find("span",class_="detail-info-right-title-font").text
            updateDate = soup.find("p",class_="title2").text
            newBooks_Dates.update({title:updateDate})
    return newBooks_Dates 

def parse(Books_Dates):
    char = ","
    keyword = "Yesterday"
    updated = []
    for title,date in Books_Dates.items():
        if char not in date or keyword not in date:
            updated.append(title)
    return updated
            
def getUpdates():
    urls = getUrls()
    html = asyncio.run(main(urls))
    return parse(scrape(html))