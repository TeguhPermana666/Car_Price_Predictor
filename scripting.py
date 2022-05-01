# Scripts data from
from email import header
from wsgiref import headers
import requests
link = requests.get("https://quikr.com/")
print(link)
# i have respone 403 => 403 the succes code

#content of requesr
print(link.content)

# confirm the object link
print(link.url)

# status the code
print(link.status_code)