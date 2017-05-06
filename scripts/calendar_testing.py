import common.helpers as helpers
import httplib2
from apiclient import discovery
import _pickle as pickle


if __name__ == '__main__':
    credentials = helpers.get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    sports_cal = '65k8839pem89hd694b6l6damdk@group.calendar.google.com'

    # load game object
    game = pickle.load(open("../tricycle_phreakz_game.pkl", "rb"))

    # parse into calendar event object
    event = game.get_gcal_dict()

    # upload event
    event = service.events().insert(calendarId=sports_cal, body=event).execute()

    print("Done!")
