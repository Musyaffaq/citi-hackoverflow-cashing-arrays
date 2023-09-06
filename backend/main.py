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
from ml_model import predict_future
from pymongo_insert import insert_to_db


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
            temp["title"] = article["title"]
            temp["description"] = article["description"]
            news_articles.append(temp)
            count += 1

    print("--- PRINT news_articles ---")
    print(news_articles)
    
    # call function from gen_ai.py by passing in news_articles
    output_insight, output_news_articles = insight(news_articles)

    print("--- PRINT output_insights ---")
    print(output_insight)

    print("--- PRINT output_news_articles ---")
    print(output_news_articles)

    keywords = ""
    for article in output_news_articles:
        keywords += article["tags"]

    insert_to_db(output_news_articles, [182.3,182.4,182.1,182.5,182.9,182.4,182.4,182.7,182.1,182.3])

    # call function from ml_model.py
    data4 = predict_future(keywords)
    print("---PRINT predict_future ---")
    print(data4)

    return jsonify({
        "insight": output_insight,
        "articles": news_articles,
        "prediction": data4
    })

if __name__ == '__main__':
    print("Running the " + os.path.basename(__file__) + " service")
    app.run(host='0.0.0.0', debug=True)
