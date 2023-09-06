from pymongo import MongoClient

def insert_to_db(news_articles, stockprice): 
    for i in range(len(news_articles)):
        news_articles['stockprice']: stockprice[i] 
    data = news_articles
    CONNECTION_STRING = "mongodb+srv://edwardsim2021:6wRN4koGWqLyHhqW@tesla-news-dates-and-ta.zrbnzax.mongodb.net/"
    client = MongoClient (CONNECTION_STRING)
    dbname = client['tesla-news']
    collection = dbname['news']

    if isinstance(data, list):
        result = collection.insert_many(data)
    else:
        result = collection.insert_one(data)
    