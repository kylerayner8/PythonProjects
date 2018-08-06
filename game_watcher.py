import time
import argparse

from scripts.generate_email import get_data, find_closest_game
from objects.game import Game

team_id_to_url_dict = {
"w" : "http://cscsports.usetopscore.com/t/estonian-thunderfrogs/schedule/event_id/active_events_only/game_type/all",
"s1" : "http://cscsports.usetopscore.com/t/estonian-thunderfrogs-1/schedule/event_id/active_events_only/game_type/all",
"s2" : "http://cscsports.usetopscore.com/t/bimmy-jutler-and-the-jyus-tones/schedule/event_id/active_events_only/game_type/all"
}

class GameWatcher(object):

    def __init__(self, team_url):
        self.team_url = team_url
        self.last_game = None
        self.next_game = None

    def run_loop(self):
        try:
            run_loop = True
            while run_loop:
                print("Checking games...")
                closest_game = get_data(self.team_url)
                if self.next_game == None or self.next_game.time != closest_game.time:
                    self.last_game = self.next_game
                    self.next_game = closest_game
                    #TODO: generate an actual gmail message
                    print(closest_game.make_email())
                else:
                    time.sleep(10)

        except Exception as e:
            raise e


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--team", required=True, type=str, choices=['s1', 's2', 'w'])
    parsed_arguments = parser.parse_args()

    watched_team = team_id_to_url_dict[parsed_arguments.team]
    watcher = GameWatcher(watched_team)
    watcher.run_loop()

