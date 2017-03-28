import requests
import constants
from bs4 import BeautifulSoup
from game import Game


def get_data(team_name):
    page = requests.get(constants.url)
    soup = BeautifulSoup(page.text, "lxml")
    try:
        team_cell = soup.find_all(string=team_name)[1]
    except IndexError:
        return Game()
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

    game_obj = Game(team_name, opponent.string, time.text, location.string, location.contents[0]['href'])
    return game_obj

for team in constants.current_teams:
    new_game = get_data(team)
    email = new_game.make_email()

    print(email)
