class Team(object):

    def __init__(self, name, wins=None, losses=None):
        self.name = name
        self.wins = wins
        self.losses = losses

        if self.wins is None:
            self.wins = 0
        if self.losses is None:
            self.losses = 0


    def update_record(self, wins, losses):
        self.wins = wins
        self.losses = losses
