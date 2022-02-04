import requests
from bs4 import BeautifulSoup

from JsonUtils import saveJson
url = "https://www.amazon.com/s"
payload = ""
headers = {
    "cookie": "lwa-context=43476f33c0a14f9ca0e189229df49ccb; session-id=142-4920380-7661759; ubid-main=130-6252755-9604445; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn=^\^L5Z9:ET^^; session-token=TZhc/cT5BakC9Rc60JKK03ySlywCGtXGw8b2ZvfQcI2rvxM0AVtuvd9Vnbw3fWm5nw764o44Mo86KXcFm4PydW4izaLnHm8wY5f7tsri2RSpxG07nWIRu/CJyBsf1q+Iej289z5ngVtBe33owA0T2pB145P0GDMSPcc510VIZHJh3owGWphyq+IY8JV/DDhK; skin=noskin; av-timezone=Africa/Addis_Ababa; csm-hit=tb:ZZZQESZ3JWD453QJQFEV+sa-D4TC7JARST4HARZBMVK7-BV76RZZFXBFGJCJQDTDR^|1642375833451&t:1642375833451&adb:adblk_no",
    "authority": "www.amazon.com",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "sec-gpc": "1",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": "https://www.amazon.com/",
    "accept-language": "en-US,en;q=0.9"
}
def singlePage(page:str)->tuple[list,dict]:
    querystring = {"k":"pastor chris oyakhilome","page":f"{page}","crid":"RS2W321LRDLA","qid":"1642375755","sprefix":"pastor chris oyakhilome^%^2Caps^%^2C219","ref":f"sr_pg_{page}"}
    #sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    soup = BeautifulSoup(response.content, 'lxml') 

    TeachingList = soup.find_all('div',class_="sg-col-4-of-12")
    Amazon_titles = []
    Amazon_Links = {}
    print(len(TeachingList))
    # print(TeachingList[18])

    for i in range(len(TeachingList)-1):
        title = TeachingList[i].find('h2').find('a').find('span').get_text()
        link = "https://www.amazon.com" + TeachingList[i].find('h2').find('a')['href']
        try:
            type = TeachingList[i].find('a',class_="a-text-bold").get_text()
        except:
            type = ''
        # https://www.amazon.com + .....
        Amazon_titles.append(title)
        Amazon_Links[title] = [link,type]
    # for Teaching in TeachingList:
    #     # print("\n\n\n\n\n",Teaching,"\n\n\n\n")
    #     # print(len(Teaching.find('img')))
    #     # title = Teaching.find('img')['alt'] 
    #     title = Teaching.find('h2').find('a').find('span').get_text()
    #     link = "https://www.amazon.com" + Teaching.find('h2').find('a')['href']
    #     # https://www.amazon.com + .....
    #     Amazon_titles.append(title)
    #     Amazon_Links[title] = link
    return Amazon_titles,Amazon_Links

def Extract():
    ATitleReal = []
    ADatabasableReal = {}
    for page in range(1,8):
        name,links = singlePage(str(page))
        ATitleReal.append(name)
        ADatabasableReal.update(links)
    saveJson('AmazonTitleList',ATitleReal)
    saveJson('AmazonDatabaseableLinkList',ADatabasableReal)


# print(name)
# print(TeachingList)
Extract()