import requests
from bs4 import BeautifulSoup

url = "https://www.booking.com/hotel/pl/happy-tower.html#tab-reviews"
response = requests.get(url)

page_dom = BeautifulSoup(response.text, 'html.parser')

reviews = page_dom.select("script[data-capla-store-data='apollo']")
review = reviews.pop(-1)
print(review)
