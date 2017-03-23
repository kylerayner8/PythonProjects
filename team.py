class Team(object):

    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0

    def update_record(self, wins, losses):
        self.wins = wins
        self.losses = losses
