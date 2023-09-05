#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script

import os
from flask import Flask, request, jsonify
from flask_cors import CORS

import json
from stock_wrapper import get_stock
from news_wrapper import get_news

app = Flask(__name__)

CORS(app)

@app.route("/")
def hello():
    return jsonify({
        "message1": "This is the backend API service for our Citi Hackoverflow Hackathon",
        "message2": "Please use the following routes:",
        "routes": [
            "/stock/<ticker>",
            "/news/<topic>"
        ]
    })

@app.route("/stock/<ticker>")
def stock(ticker):
    return jsonify(get_stock(ticker.upper()))

@app.route("/news/<topic>")
def news(topic):
    return jsonify(get_news(topic))

# @app.route("/inventory/<string:type>")
# def find_by_type(type):
#     inventory = Inventory.query.filter_by(type=type).first()
#     if inventory:
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": inventory.json()
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "data": {
#                 "type": type
#             },
#             "message": "Inventory not found."
#         }
#     ), 404


# @app.route("/inventory/return/<string:type>", methods=['PUT'])
# def update_inventory(type):
#     try:
#         inventory = Inventory.query.filter_by(type=type).first()
#         if not inventory:
#             return jsonify(
#                 {
#                     "code": 404,
#                     "data": {
#                         "inventory": inventory
#                     },
#                     "message": "inventory not found."
#                 }
#             ), 404

#         # update status
#         data = request.get_json()
#         if data['quantity']:
#             quantity_return = data['quantity']

#             if quantity_return > int(inventory.loaned):
#                 return jsonify(
#                     {
#                         "code": 406,
#                         "quantity": quantity_return,
#                         "data": inventory.json(),
#                         "message": "Quantity to be returned is more than the loaned quantity."
#                     }
#                 ), 406

#             available = int(inventory.available) + int(quantity_return)
#             loaned = int(inventory.loaned) - int(quantity_return)
#             inventory.available = available
#             inventory.loaned = loaned
#             db.session.commit()
#             return jsonify(
#                 {
#                     "code": 200,
#                     "data": inventory.json()
#                 }
#             ), 200
#     except Exception as e:
#         return jsonify(
#             {
#                 "code": 500,
#                 "data": {
#                     "type": type
#                 },
#                 "message": "An error occurred while updating the inventory. " + str(e)
#             }
#         ), 500


# @app.route("/inventory/loan/<string:type>", methods=['PUT'])
# def loan_inventory(type):
#     try:
#         inventory = Inventory.query.filter_by(type=type).first()
#         if not inventory:
#             return jsonify(
#                 {
#                     "code": 404,
#                     "data": {
#                         "inventory": inventory
#                     },
#                     "message": "inventory not found."
#                 }
#             ), 404

#         # update status
#         data = request.get_json()
#         if data['quantity']:
#             quantity_loan = data['quantity']

#             if quantity_loan > int(inventory.available):
#                 return jsonify(
#                     {
#                         "code": 406,
#                         "quantity": quantity_loan,
#                         "data": inventory.json(),
#                         "message": "Quantity to be returned is more than the loaned quantity."
#                     }
#                 ), 406

#             available = int(inventory.available) - int(quantity_loan)
#             loaned = int(inventory.loaned) + int(quantity_loan)
#             inventory.available = available
#             inventory.loaned = loaned
#             db.session.commit()
#             return jsonify(
#                 {
#                     "code": 200,
#                     "data": inventory.json()
#                 }
#             ), 200
#     except Exception as e:
#         return jsonify(
#             {
#                 "code": 500,
#                 "data": {
#                     "type": type
#                 },
#                 "message": "An error occurred while updating the inventory. " + str(e)
#             }
#         ), 500


if __name__ == '__main__':
    print("Running the " + os.path.basename(__file__) + " service")
    app.run(host='0.0.0.0', debug=True)
