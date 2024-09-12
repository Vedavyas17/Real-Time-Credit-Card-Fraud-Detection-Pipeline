from pymongo import MongoClient
from kafka import KafkaConsumer
from json import loads

client = MongoClient('localhost', 27017)
db = client['capstoneproject']
