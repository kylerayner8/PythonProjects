import requests
import constants
from bs4 import BeautifulSoup
import os


def get_season_data():
    cur_season = constants.current_season_index
    end_index = cur_season - 1
    results = open("results.txt", 'w')

    while cur_season > end_index:
        url = constants.base_season_url.format(cur_season)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "lxml")

        headings = soup.findAll('span', class_="pagLeagueHeading")
        we_played = False
        for heading in headings:
            text_field = heading.text.lower()
            if 'sunday' in text_field and 'rec' in text_field:
                we_played = True

        if we_played is True:
            results.write(str(cur_season))
            results.write('\n')
        cur_season = cur_season - 1

    results.close()
    return None

if 'results.txt' in os.listdir():
    os.remove('results.txt')
#get_season_data()

print("hello")
