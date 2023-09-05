#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script

import os
from flask import Flask, request, jsonify
from flask_cors import CORS

import json
from stock_wrapper import get_stock
from news_wrapper import get_news
from gen_ai import insight
from ml_model import predict
from pymongo_get_database import get_database


app = Flask(__name__)

CORS(app)

@app.route("/")
def hello():
    return jsonify({
        "message1": "This is the backend API service for our Citi Hackoverflow Hackathon",
        "message2": "Please use the following routes:",
        "routes": [
            "/create_insight/<ticker>/<topic>",
            "/stock/<ticker>",
            "/news/<topic>"
        ]
    })

# to get the stock prices of a ticker
@app.route("/stock/<ticker>")
def stock(ticker):
    return jsonify(get_stock(ticker.upper()))

# to get news of certain topics
# might need to parse the topic
@app.route("/news/<topics>")
def news(topics):
    return get_news(topics)

@app.route("/create_insight/<ticker>/<topics>")
def create_insight(ticker, topics):

    # call function from stock_wrapper.py
    data1 = get_stock(ticker.upper())
    
    # call function from news_wrapper.py
    data2 = get_news(topics)
    articles = data2["articles"]
    count = 0
    news_articles = []
    for article in articles:
        temp = {}
        if count == 10:
            break
        if article["title"] != "[Removed]":
            temp["content"] = article["title"] + article["description"]
            temp["url"] = article["url"]
            temp["date"] = article["publishedAt"]
            news_articles.append(temp)
            count += 1

    print(news_articles)
    
    # call function from gen_ai.py by passing in news_articles
    data3 = insight()

    toInsertDB = {}

    # insert into database
    # dbname = get_database()
    # collection_name = dbname["news"]
    # collection_name.insert_one(toInsertDB)

    # call function from ml_model.py
    data4 = predict()

    return jsonify({
        "message": "Need to parse through the ticker and topic"
    })

if __name__ == '__main__':
    print("Running the " + os.path.basename(__file__) + " service")
    app.run(host='0.0.0.0', debug=True)
