import constants

class Game(object):

    def __init__(self, team=None, opponent=None, time=None, location=None, directions=None):
        self.team = team
        self.opponent = opponent
        self.time = time
        self.location = location
        self.directions = directions

    def make_email(self):
        email_string = constants.email.format(self.team, self.opponent, self.time, self.location)
        return email_string


    def __str__(self):
        return "{0}:{1}:{2}:{3}".format(self.team, self.opponent, self.time, self.location)
