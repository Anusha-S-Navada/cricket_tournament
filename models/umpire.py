import random


class Umpire:
    def __init__(self, teams, field):
        self.teams = teams
        self.field = field
        self.scores = {team: 0 for team in teams}
        self.wickets = {team: 0 for team in teams}
        self.overs = 0
        self.current_bowler = None
        self.balls = 0

    def simulate_ball(self):
        batsman = random.choice(self.teams[0].players)
        bowler = self.current_bowler or random.choice(self.teams[1].players)
        outcome = random.choices(['run', 'out', 'no_ball', 'wide_ball'], weights=[0.6, 0.2, 0.1, 0.1], k=1)[0]
        if outcome == 'run':
            runs = random.choices([0, 1, 2, 3, 4, 6], weights=[0.1, 0.4, 0.2, 0.1, 0.15, 0.05], k=1)[0]
            self.scores[self.teams[0]] += runs
        elif outcome == 'out':
            self.wickets[self.teams[0]] += 1
            self.current_bowler = self.teams[1].choose_bowler()
        elif outcome == 'no_ball':
            runs = random.choices([1, 2, 3, 4, 6], weights=[0.4, 0.2, 0.1, 0.2, 0.1], k=1)[0]
            self.scores[self.teams[0]] += runs
        elif outcome == 'wide_ball':
            self.scores[self.teams[0]] += 1

        self.balls += 1
        if self.balls % 6 == 0:
            self.start_over()

        self.overs = self.balls // 6 + (self.balls % 6) / 10

        return batsman, bowler, outcome

    def start_over(self):
        self.balls = 0
        self.current_bowler = self.teams[1].choose_bowler()
