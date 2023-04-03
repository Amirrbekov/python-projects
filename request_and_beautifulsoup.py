import requests

from bs4 import BeautifulSoup

url = "https://github.com/Amirrbekov"

response = requests.get(url)

html = response.content

soup = BeautifulSoup(html, "html.parser")

print(soup.prettify())