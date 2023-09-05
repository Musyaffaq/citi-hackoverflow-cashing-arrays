# https://newsapi.org/

import requests
from flask import jsonify
import os
from dotenv import load_dotenv

def get_news(topics):
    api_key = os.getenv("NEWS_API_KEY")
    url = "https://newsapi.org/v2/everything?q=" + topics + "&sortBy=publishedAt&language=en&apiKey=" + api_key
    r = requests.get(url)
    data = r.json()

    return data