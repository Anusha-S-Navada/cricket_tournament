from models.match import Match
from utils.helpers import create_players, create_teams, create_field, play_match

# Create players
players = create_players()

# Create teams
team1, team2 = create_teams(players)

# Create field
field = create_field()

# Create match and play
match = Match(team1, team2, field)
play_match(match)
