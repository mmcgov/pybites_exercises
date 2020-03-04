from collections import namedtuple
import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"
Game = namedtuple('Game', 'title link')


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    games_info = list()
    data = feedparser.parse(FEED_URL)
    for game in range(len(data.entries)):
        game_data = Game(data.entries[game]['title'],
                         data.entries[game]['link'])
        games_info.append(game_data)
    return games_info
