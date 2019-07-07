# https://roche.io/2016/05/scrape-wikipedia-with-python

import requests
from bs4 import BeautifulSoup

WIKI_URL = "https://en.wikipedia.org/wiki/List_of_tallest_buildings_and_structures"

req = requests.get(WIKI_URL)
soup = BeautifulSoup(req.content, 'lxml')
table_classes = {"class": ["sortable", "plainrowheaders"]}
wikitables = soup.findAll("table", table_classes)

print(wikitables)