import constants

class Game(object):

    def __init__(self, team=None, opponent=None, time=None, location=None, directions=None):
        self.team = team
        self.opponent = opponent
        self.time = time
        self.location = location
        self.directions = directions
        self.email_str = "{time}\n{team} vs. {opp}\n{location}"

    def make_email(self):
        # Generates a string that describes the game for usage in an email
        formatted_time = self.time.strftime("%I:%M %p").lstrip("0")
        location_translation = constants.locations_mapping.get(self.location, self.location)
        email_string = self.email_str.format(team=self.team, opp=self.opponent, 
                                             time=formatted_time, location=location_translation)
        return email_string


    def get_gcal_dict(self):
        end_hour = self.time.hour + 1
        event = {
            'summary': '{0} vs. {1}'.format(self.team, self.opponent),
            'location': self.location,
            'description': 'Game event',
            'start': {
                'dateTime': self.time.isoformat(),
                'timeZone': 'US/Central'
            },
            'end': {
                'dateTime': self.time.replace(hour=end_hour).isoformat(),
                'timeZone': 'US/Central'
            },
            'attendees': [],
            'reminders': {
                'useDefault': True,
                'overrides': [],
            },
        }

        return event


    def __str__(self):
        return "{0}:{1}:{2}:{3}".format(self.team, self.opponent, self.time, self.location)
