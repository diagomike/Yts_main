import requests
#1944
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

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)