from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

client = MongoClient(os.getenv("CONNECTION_URL"))
db = client.myDB
collection = db['tasks']
