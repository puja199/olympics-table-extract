# import the library used to download a web content
import urllib2

# import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

# import csv library to export data into csv
import csv

# Download the website and return the html to the variable 'page'
page = urllib2.urlopen("https://en.wikipedia.org/wiki/2018_Winter_Olympics_medal_table")

# Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page, "html.parser")
all_tables = soup.find_all('table')
olympics_table = soup.find('table', class_='wikitable sortable plainrowheaders')

data = []
description_header = olympics_table.find("tr")

for row in olympics_table.findAll("tr"):
    if row.find('td'):
        olympics_achievement_country = []
        country = row.find('th').find('a').string
        medals = row.findAll('td')
        if len(medals) == 5:
            medals.pop(0)
        olympics_achievement_country.append(country)
        for medal in medals:
            olympics_achievement_country.append(int(str(medal.string).replace('\n', '')))
        data.append(olympics_achievement_country)
        with open("data.csv", "w") as output:
            writer = csv.writer(output)
            writer.writerows(data)
