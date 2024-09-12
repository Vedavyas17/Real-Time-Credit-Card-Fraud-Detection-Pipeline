from pymongo import MongoClient
from kafka import KafkaConsumer
from json import loads

client = MongoClient('localhost', 27017)
db = client['capstoneproject']

def readKafka():
    consumer = KafkaConsumer(
        'transactions-topic-verified',
        bootstrap_servers=['18.211.252.152:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        value_deserializer=lambda x: loads(x.decode('utf-8')))
    return consumer

def readMongoLookup():
    try:
        lookup_transaction = db.lookupTrans
        print("Connection Successful")
    except:
        print("Connection to MongoDB is unsuccessful")
    return lookup_transaction

def writeToMongo(transaction):
    collection_name = db.cardTransactions
    rec_id = collection_name.insert_one(transaction)
    print("The data is inserted with Record ID", rec_id)