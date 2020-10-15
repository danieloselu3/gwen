# imports
import requests

# target url
url = "https://api.betika.com/v1/uo/matches?.json"

# get our url
games = requests.get(url).json()

# todays games
games_container = games['data']

# loop and display the games
for game in games_container:
    home_team = game['home_team']
    away_team = game['away_team']
    print('{} vs {}'.format(home_team, away_team))

