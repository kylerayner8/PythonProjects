import _pickle as pickle
import requests
from bs4 import BeautifulSoup
import constants
import datetime

from objects.game import Game


def get_data(team_name):
    page = requests.get(constants.url)
    soup = BeautifulSoup(page.text, "lxml")
    try:
        team_cell = soup.find_all(string=team_name)[1]
    except IndexError:
        return None
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

    dt = datetime.datetime.strptime(time.string, '%m/%d/%Y %I:%M:%S %p')
    game_obj = Game(team_name, str(opponent.string), dt, str(location.string), str(location.contents[0]['href']))
    return game_obj

if __name__ == "__main__":
    for team in constants.current_teams:
        new_game = get_data(team)
        # If saving the game is desired for some reason...
        # file_name = "{0}_game.pkl".format(team.lower())
        # file_name = file_name.replace(" ", "_")
        # file_name = file_name.replace("#", "")
        # file = open(file_name, 'wb')
        # pickle.dump(new_game, file)
        # file.close()
        email = new_game.make_email()

        print(email)
