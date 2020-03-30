#Dignitas Score Scraper

import csv, json, requests, sys
from bs4 import BeautifulSoup

headers = {
        'User-Agent': 'Matthew Pigram. matthewpigram.co.uk',
        'From': 'matthew.pigram2@gmail.com'
}

url = 'https://www.hltv.org/results?team=5422'
page = requests.get(url, headers=headers)
page = requests.get('https://www.hltv.org/results?team=5422')

soup = BeautifulSoup(page.text, 'html.parser')

nav_links = soup.find(class_='pagination-component pagination-bottom')
nav_links.decompose()

team_score = soup.select(class_='results')[:50]
team_score_items = team_score.find_all('div')

for team_score in team_score_items:
    print(team_score.get_text())
