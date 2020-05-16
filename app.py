import os
from flask import Flask, jsonify
from pymongo import MongoClient


app = Flask(__name__)
client = MongoClient(port=27017)
db = client.sample_db


@app.route("/")
def index():
    _items = db.sample_collection.find()
    items = [items for items in _items]

    return jsonify({'hello_world': items})


if __name__ == "__main__":
    print('Running container')
    app.run(host="0.0.0.0", debug=True)
