from pymongo import MongoClient
CONNECTION_STRING = "mongodb+srv://edwardsim2021:6wRN4koGWqLyHhqW@tesla-news-dates-and-ta.zrbnzax.mongodb.net/"
client = MongoClient (CONNECTION_STRING)
dbname = client['tesla-news']
collection = dbname['news']

documents = list(collection.find())
keywords = [doc['keywords'] for doc in documents]
stockprices = [doc['stockprice'] for doc in documents]

from sklearn.feature_extraction.text import TfidfVectorizer
keywords_text = [k.replace(',', ' ') for k in keywords]
print(keywords_text)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(keywords_text)
y  = stockprices

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

from sklearn.metrics import mean_squared_error



new_keywords = 'bearish, loss, decline, downtrend'
new_keywords_text = " ".join(new_keywords)
new_X = vectorizer.transform([new_keywords_text])
predicted_stock_price = model.predict(new_X)[0]
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"Predicted Stock Price: {predicted_stock_price}")

