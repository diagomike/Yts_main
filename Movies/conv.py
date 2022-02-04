from bs4 import BeautifulSoup
from JsonUtils import *
import asyncio
import httpx
import time

url = "https://yts.mx/browse-movies/0/all/all/0/likes/0/all"

querystring = {"page":"2"}

payload = ""
headers = {
    "authority": "yts.mx",
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
    "sec-gpc": "1",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://yts.mx/browse-movies/0/all/all/0/likes/0/all?page=2",
    "accept-language": "en-US,en;q=0.9",
    "cookie": "PHPSESSID=vl75p9vi5tskv72km0283lrmg8; __cf_bm=SH8q1OTscIh2WRjUG1u46pF3aYz4jMb04.ZLmNm7yLE-1643988228-0-ARq2n4da30eu8iFYkg3i0jwkk4aCMvWtO9LibF3+WNyOvQfDbmny+i8zn1VPkouT/bUpqfXIGP1b1eWCsfjNKB9usAJDyPnXQCGQRB8P9lTKug0DnunG8Lt4NXsKO9/vrw=="
}
async def log_request(request):
    print(f"Request: {request.method} {request.url}")

async def log_response(respose):
    request = respose.request
    print(f"Response: {request.method} {request.url} - Status {respose.status_code}")

async def trace_page(response):
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup.prettify())
    tree = soup.find_all('a',class_="browse-movie-link")
    all_links =[]
    for item in tree:
        all_links.append(item['href'])
        # print(item['href'])
    return all_links

async def get_episode(ep_id: int):
    async with httpx.AsyncClient(event_hooks={'request': [log_request], 'response':[log_response]},timeout=None) as client:
        r = await client.request("GET", url, data=payload, headers=headers, params={"page":f"{ep_id}"}) #(f'https://rickandmortyapi.com/api/episode/{ep_id}')
        #results.append(r.json())
        time.sleep(.02)
        all_links.extend(await trace_page(r))
        return

async def main(rangel,ranger):
    tasks = []
    for ep_id in range(rangel,ranger+1):
        tasks.append(get_episode(ep_id))
    await asyncio.gather(*tasks)

# results = []
all_links = []
def runner_up(limit,start=2):
    ran_ge = 150
    section = limit/float(ran_ge)
    for part in range(section.__ceil__()):
        r = part*ran_ge
        time.sleep(5)
        try:
            asyncio.run(main(r,r+ran_ge))
            print("Completed Successfully!!")
            saveJson("all_links"+str(part),all_links)
        except:
            print("stopped With Errors!")
            saveJson("all_links"+str(part),all_links)

runner_up(1944)
    




