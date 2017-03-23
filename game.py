import constants

class Game(object):

    def __init__(self, team, opponent, time, location):
        self.team = team
        self.opponent = opponent
        self.time = time
        self.location = location

    def make_email(self):
        email_string = constants.email.format(self.team, self.opponent, self.time, self.location)
        return email_string
