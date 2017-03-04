import requests
import template
from bs4 import BeautifulSoup


def get_data(team_name):
    page = requests.get(template.url)
    soup = BeautifulSoup(page.text, "lxml")
    team_cell = soup.find_all(string=team_name)[1]
    game_row = team_cell.find_parent().find_parent()
    children = game_row.contents
    time = children[1]
    location = children[3]
    team1 = children[5]
    team2 = children[7]
    if team1.contents[0] == team_name:
        opponent = team2.contents[0]
    else:
        opponent = team1.contents[0]
    game_info = {
        "time": time.text,
        "location": location.string,
        "opponent": opponent.string
    }
    new_email = template.email.format(team_name, opponent, time.text,
                                      location.string)
    print(new_email)
    return game_info

get_data("Estonian Thunderfrogs")
get_data("Tay Klompson and the Laun Shivingstons")
