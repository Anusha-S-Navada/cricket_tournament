class Commentator:
    def __init__(self, umpire):
        self.umpire = umpire

    def comment_ball(self):
        batsman, bowler, outcome = self.umpire.simulate_ball()
        if outcome == 'run':
            print(f"{batsman.name} scores runs against {bowler.name}.")
        elif outcome == 'out':
            print(f"{batsman.name} is out! {bowler.name} takes a wicket!")
        elif outcome == 'no_ball':
            print(f"{bowler.name} bowls a no ball. Runs added to the team's score.")
        elif outcome == 'wide_ball':
            print(f"{bowler.name} bowls a wide ball. Extra run added to the team's score.")
        print(f"Score: {self.umpire.scores[self.umpire.teams[0]]}/{self.umpire.wickets[self.umpire.teams[0]]} in {self.umpire.overs} overs.")
