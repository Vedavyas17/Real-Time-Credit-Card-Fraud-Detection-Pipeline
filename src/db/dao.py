from pymongo import MongoClient
from kafka import KafkaConsumer
from json import loads

client = MongoClient('localhost', 27017)
db = client['capstoneproject']

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