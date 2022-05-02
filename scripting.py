# Scripts data from
import requests
headers= {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}
link = requests.get("https://quikr.com/",headers=headers)
# print(link)
# i have respone 403 => 403 the succes code

#content of requesr
# print(link.content)

# confirm the object link
# print(link.url)

# status the code
# print(link.status_code)

from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs

soup = BeautifulSoup(link.content,"html.parser")
# print(soup.prettify())

# get the title
print(soup.title)

# get the name of tag
print(soup.title.name)

# get the parent tage
print(soup.title.parent.name)

s = soup.find('div', class_='entry-content')
content = s.find_all('p')