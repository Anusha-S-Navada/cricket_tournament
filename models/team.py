import random


class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.captain = None
        self.batting_order = []

    def select_captain(self):
        self.captain = random.choice(self.players)

    def choose_bowler(self):
        return random.choice(self.players)

    def send_next_player(self):
        if self.batting_order:
            return self.batting_order.pop(0)
        else:
            return None

    def set_batting_order(self, order):
        self.batting_order = order
