import requests
import json

def search(query):
    r = requests.get(f"https://torrents-csv.com/service/search?q={query}").text
    data = json.loads(r)
    return data