from pymongo import MongoClient
import pickle
CONNECTION_STRING = "mongodb+srv://edwardsim2021:6wRN4koGWqLyHhqW@tesla-news-dates-and-ta.zrbnzax.mongodb.net/"
client = MongoClient (CONNECTION_STRING)
dbname = client['tesla-news']
collection = dbname['news']

def train_and_pickle_model(): 

    documents = list(collection.find())
    keywords = [doc['tags'] for doc in documents]
    stockprices = [doc['stockprice'] for doc in documents]

    from sklearn.feature_extraction.text import TfidfVectorizer
    keywords_text = [k.replace(',', ' ') for k in keywords]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(keywords_text)
    y  = stockprices
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X_train, y_train)

    with open ('linear_regression_model.pkl', 'wb') as file: 
        pickle.dump(model, file)
    print('done')

