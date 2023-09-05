from pymongo_get_database import get_database

news = {   
"Date": '6/9/2023',
"Stock": "TSLA",
"Keywords": "EV, stock, upturn, positive"
} 
dbname = get_database()
 
# Retrieve a collection named "user_1_items" from database
collection_name = dbname["news"]

collection_name.insert_one(news)   