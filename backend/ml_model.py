import pickle
from sklearn.metrics import mean_squared_error
from sklearn.feature_extraction.text import TfidfVectorizer
from pymongo import MongoClient
vectorizer = TfidfVectorizer()

with open('linear_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

CONNECTION_STRING = "mongodb+srv://edwardsim2021:6wRN4koGWqLyHhqW@tesla-news-dates-and-ta.zrbnzax.mongodb.net/"
client = MongoClient (CONNECTION_STRING)
dbname = client['tesla-news']
collection = dbname['news']
documents = list(collection.find())
keywords = [doc['keywords'] for doc in documents]

vectorizer.fit(keywords)

new_keywords = 'bearish, loss, decline, downtrend'
new_keywords_text = " ".join(new_keywords)
new_X = vectorizer.transform([new_keywords_text])
predicted_stock_price = model.predict(new_X)[0]
print(f"Predicted Stock Price: {predicted_stock_price}")

