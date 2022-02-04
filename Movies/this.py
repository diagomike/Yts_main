import codecs
from bs4 import BeautifulSoup

file = codecs.open("page.html", "r", "utf-8")
soup = BeautifulSoup(file.read(), 'html.parser')
# print(soup.prettify())
tree = soup.find_all('a',class_="browse-movie-link")
all_links =[]
for item in tree:
    all_links.append(item['href'])
    print(item['href'])
#body > div.main-content > div.browse-content > div > section > div > div:nth-child(1)


print(len(all_links))