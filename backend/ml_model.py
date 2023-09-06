import numpy as np
import pickle
from sklearn.metrics import mean_squared_error
from sklearn.feature_extraction.text import TfidfVectorizer
from pymongo import MongoClient
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm 


vectorizer = TfidfVectorizer()



def predict_future(new_keywords): 
    with open('linear_regression_model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    #loading prerequisites and measuring accuracy of current model
    CONNECTION_STRING = "mongodb+srv://edwardsim2021:6wRN4koGWqLyHhqW@tesla-news-dates-and-ta.zrbnzax.mongodb.net/"
    client = MongoClient (CONNECTION_STRING)
    dbname = client['tesla-news']
    collection = dbname['news']
    documents = list(collection.find())
    keywords = [doc['keywords'] for doc in documents]
    keywords_text = [k.replace(',', ' ') for k in keywords]
    stockprices = [doc['stockprice'] for doc in documents]
    X = vectorizer.fit_transform(keywords_text)
    y  = stockprices
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    y_pred_before = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred_before)
    rmse = np.sqrt(mse)
    r2 = model.score(X_train, y_train)
    print(y_pred_before, mse, r2, rmse)

    #predicting function
    new_keywords_text = [new_keywords.replace(',', ' ')] 
    new_X = vectorizer.transform(new_keywords_text)
    predicted_stock_price = model.predict(new_X)
    return {
        "predicted_price" : predicted_stock_price,
        "mse": mse, 
        "rmse": rmse, 
        "r2": r2
    }

    

