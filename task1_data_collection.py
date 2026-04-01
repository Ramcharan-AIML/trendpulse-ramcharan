import requests
import json
import time
from datetime import datetime

# First i am taking the Id's of the top stories
ids_url = "https://hacker-news.firebaseio.com/v0/topstories.json"

headers = {"User-Agent": "TrendPulse/1.0"}

response_ids = requests.get(ids_url , headers = headers)

story_ids = response_ids.json()
print(story_ids)


# Taking the categories to match the keywords in the title of the API
categories = {
    "technology": ["ai", "software", "tech", "programming", "computer"],
    "science": ["nasa", "space", "research", "physics", "biology"],
    "sports": ["football", "cricket", "nba", "match", "tournament"],
    "worldnews": ["government", "election", "war", "policy"],
    "entertainment": ["movie", "music", "netflix", "film"]
}


# defining the function for matching the title by the keywords in the categories section
def assigned_keyword(title):
    title = title.lower()

    for category, keywords in categories.items():
        if keyword in title:
            return keyword
    return None






