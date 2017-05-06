import constants
import time
import httplib2
from apiclient import discovery
from scripts.generate_email import get_data
import common.helpers as helpers


def main():
    loop = True
    while loop:
        print("loop")
        # Check the website for games
        game_list = []
        for team in constants.current_teams:
            print("Getting data for {0}".format(team))
            game_obj = get_data(team)
            if game_obj:
                game_list.append(game_obj)

        # Make calendar events for new games
        credentials = helpers.get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('calendar', 'v3', http=http)

        sports_cal = '65k8839pem89hd694b6l6damdk@group.calendar.google.com'

        # parse into calendar event object
        for game in game_list:
            event = game.get_gcal_dict()

            # upload event
            response = service.events().insert(calendarId=sports_cal, body=event).execute()
        loop = False
        # # Slow down the loops
        # time.sleep(10)

if __name__ == "__main__":
    main()
