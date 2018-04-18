import _pickle as pickle
import requests
from bs4 import BeautifulSoup
import constants
import datetime

from objects.game import Game


def find_closest_game(games_list):
    now = datetime.datetime.now()
    closest_game = None
    closest_gap = None
    # games_list.reverse()

    for game in games_list:
        now_to_new_game_time = game.time - now
        # close_game_to_new_game_time = game.time - closest_game.time
        # Ignore the game if it's already happened
        if now_to_new_game_time.total_seconds() < 0:
            pass
        else:
            if closest_game == None:
                closest_game = game
                closest_gap = now_to_new_game_time
            elif closest_gap.total_seconds() > now_to_new_game_time.total_seconds():
                closest_game = game
                closest_gap = now_to_new_game_time

    return closest_game


def get_data(team_url):
    page = requests.get(team_url)
    soup = BeautifulSoup(page.text, "lxml")
    
    try:
        game_list = soup.find("div", {"id":"game-list"})
    except IndexError:
        return None
    
    list_of_games = game_list.find_all("div", class_="row-fluid")
    games_list = list()
    for game in list_of_games:
        info_list = game.find_all("div")
        teams = game.find_all("div", class_="schedule-team-name")
        
        date_time = info_list[0]
        date = date_time.find(class_="push-left").text
        time = date_time.find(class_="push-right").text.strip()
        full_date_string = date + " " + time

        location = game.find_all(class_="span2")[-1].find("span").text
        parsed_location = " ".join(location.split())

        dtobj = datetime.datetime.strptime(full_date_string, "%a, %b %d, %Y %I:%M %p")

        new_game = Game(teams[0].text.strip(), teams[1].text.strip(), dtobj, parsed_location)
        games_list.append(new_game)

    closest_game = find_closest_game(games_list)

    return closest_game


if __name__ == "__main__":
    closest_game = get_data("http://cscsports.usetopscore.com/t/estonian-thunderfrogs/schedule/event_id/active_events_only/game_type/all")
    print(closest_game.make_email())
