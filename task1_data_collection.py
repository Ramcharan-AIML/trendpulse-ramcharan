import requests
import json
import time
import os
from datetime import datetime

# First i am taking the Id's of the top stories
ids_url = "https://hacker-news.firebaseio.com/v0/topstories.json"

headers = {"User-Agent": "TrendPulse/1.0"}

response_ids = requests.get(ids_url , headers = headers)

story_ids = response_ids.json()


# Taking the categories to match the keywords in the title of the API
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}


# defining the function for matching the title by the keywords in the categories section
def assigned_keyword(title):
    title = title.lower()

    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in title:
                return category
    return None

# Taking the empty list for storing all data after getting the top stories list 
collection_total_data = []


# Maintaining the category count for upto 25
category_count = {
    "technology": 0,
    "science": 0,
    "sports": 0,
    "worldnews": 0,
    "entertainment": 0
}


# Fetch each story and process

for story_id in story_ids:

    # all_full = True

    # for count in category_count.values():
    #     if count >= 25:
    #         all_full = False
    #         break
    # if all_full:
    #     break

    # Stop if count reaches to the 25 limit 
    if all(count >=25 for count in category_count.values()):
        break


    # Taking the stories by id's 
    url_story = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"


    # Using try except method for exception handling to find the errors
    try:
        response = requests.get(url_story , headers=headers)
        # checking status code , if it is 200, load the data from the api 
        if response.status_code == 200:
            data = response.json()
        else:
            continue

        # checking the title is there or not in the data
        if "title" in data:
            category = assigned_keyword(data["title"])
        else:
            continue

        if data is None:
            continue

        # if category is not there , skip to next
        if category is None:
            continue

        # if the count in the category has already above 25 , skip the step
        if category_count[category] >=25:
            continue


        # collecting the all the fields from the api
        required_record = {
            "post_id": data.get("id"),
            "title": data.get("title"),
            "subreddit": category,   # our assigned category
            "score": data.get("score", 0),
            "num_comments": data.get("descendants", 0),
            "author": data.get("by"),
            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        collection_total_data.append(required_record)

        category_count[category] += 1

        # print(f"Collected {category}: {category_count[category]}")


    except Exception as error:
        print(f"Error occured with status code{error}")

            
    time.sleep(1)

print(collection_total_data)


# saving the total final data into the data folder
os.makedirs("data" , exist_ok=True)

filename = f"data/trends_{datetime.now().strftime("%y%m%d")}.json"

# Using file handling we are dumping the data into json format
with open(filename , "w" , encoding="utf-8") as f:
    json.dump(collection_total_data , f , indent=4)

print(f"Collected  {len(collection_total_data)} stories. Saved to {filename}")
# print(f"length of the data is {len(collection_total_data)}")
# print(f"data saved in {filename}")
