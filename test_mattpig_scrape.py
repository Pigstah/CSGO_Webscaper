# Import Libraries
import csv
import requests
from bs4 import BeautifulSoup

# Identifiable information
headers = {
    'User-Agent': 'Matthew Pigram, matthewpigram.co.uk',
    'From': 'matthew.pigram2@gmail.com'
}

url = 'https://matthewpigram.co.uk'

page = requests.get(url, headers = headers)

page = requests.get('https://matthewpigram.co.uk/')

# Create BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# Remove bottom links
#skills = soup.find(class_='skills-mobile-img')
#skills.decompose()

# Create a file to write to, add headers row
f = csv.writer(open('skills-test.csv', 'w'))
f.writerow(['Text'])

# Pull all text from the skills-statement div
skills_statement_list = soup.find(class_='skills-statement-container')

# Pull text from all instances of <a> tag within BodyText div
skills_statement_list_items = skills_statement_list.find_all('h1')

# Create for loop to print out all artists' names
#for skills_statement in skills_statement_list_items:
text = skills_statement_list.contents

    # Add each artist's name and associated link to a row
f.writerow([text])

#print(skills_statement_list)

