import random
from models.player import Player
from models.team import Team
from models.field import Field


def create_players():
    # Create and return a list of players
    players = [
        Player("MS Dhoni", 0.8, 0.2, 0.99, 0.8, 0.9),
        Player("Virat Kohli", 0.9, 0.1, 0.95, 0.7, 0.8),
        Player("Rohit Sharma", 0.85, 0.1, 0.9, 0.8, 0.85),
        Player("Jasprit Bumrah", 0.3, 0.9, 0.8, 0.5, 0.7),
        Player("Ravindra Jadeja", 0.7, 0.7, 0.9, 0.6, 0.8),
        Player("Shikhar Dhawan", 0.8, 0.1, 0.8, 0.8, 0.7),
        Player("Hardik Pandya", 0.7, 0.5, 0.8, 0.7, 0.6),
        Player("Yuzvendra Chahal", 0.2, 0.8, 0.7, 0.4, 0.6),
        Player("KL Rahul", 0.8, 0.1, 0.8, 0.8, 0.7),
        Player("Mohammed Shami", 0.3, 0.7, 0.7, 0.6, 0.6)
    ]
    return players


def create_teams(players):
    # Create and return two teams with the given players
    team1 = Team("India", players[:5])
    team2 = Team("Australia", players[5:])
    return team1, team2


def create_field():
    # Create and return a Field object with desired attributes
    field = Field("Large", 0.8, "Dry", 0.1)
    return field


def play_match(match):
    match.start_match()
    while match.umpire.wickets[match.team1] < 10 and match.current_inning <= 2:
        match.commentator.comment_ball()

        if match.umpire.overs >= 2.0 and match.current_inning == 1:
            print("End of the innings.")
            match.change_innings()

    print("Match ended.")
