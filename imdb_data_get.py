import requests

from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

response = requests.get(url)

html = response.content

soup = BeautifulSoup(html, "html.parser")

a = float(input("Minimum rating: "))

names = soup.find_all("td", {"class":"titleColumn"})
ratings = soup.find_all("td", {"class":"ratingColumn imdbRating"})

for name,rating in zip(names,ratings):
    
    name = name.text
    rating = rating.text
    
    name = name.strip()
    name = name.replace("\n","")
    
    if float(rating) > a:
        print(f"Film name {name}, rating {rating}")
    
"""    print("Name: ", name)
    print("Rating: ", rating)"""