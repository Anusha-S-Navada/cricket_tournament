from models.umpire import Umpire
from models.commentator import Commentator


class Match:
    def __init__(self, team1, team2, field):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.umpire = None
        self.commentator = None
        self.current_inning = 1

    def start_match(self):
        self.team1.select_captain()
        self.team2.select_captain()
        self.team1.set_batting_order(self.team1.players)
        self.umpire = Umpire([self.team1, self.team2], self.field)
        self.commentator = Commentator(self.umpire)

    def change_innings(self):
        self.current_inning += 1
        self.team1, self.team2 = self.team2, self.team1
        self.start_match()

    def play_match(self):
        self.start_match()
        while self.umpire.wickets[self.team1] < 10 and self.current_inning <= 2:
            self.commentator.comment_ball()

            if self.umpire.overs >= 2.0 and self.current_inning == 1:
                print("End of the innings.")
                self.change_innings()

        print("Match ended.")
