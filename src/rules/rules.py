import sys
sys.path.append("..")
from db.geo_map import GEO_Map
from db.dao import *
from datetime import datetime

# Read the transaction data from the lookup table in MongoDB
collection_lookup = readMongoLookup()

def processMessage(msg):
    card_id = msg['card_id']
    document = {}
    cursor = collection_lookup.find({"card_id": card_id})
    
    for document in cursor:
        document = document
    
    status = authoriseTransaction(msg, document)
    return status

def authoriseTransaction(transaction_data, lookup_data):
    auth = ""
    
    # Check UCL
    if transaction_data['amount'] <= lookup_data['UCL']:
        auth = "GENUINE"
    else:
        auth = "FRAUD"
    
    # Check Credit Score
    if lookup_data["score"] < 200:
        auth = "FRAUD"
    
    # Check Speed
    dist = calcDist(transaction_data, lookup_data)
    time = calcTime(transaction_data, lookup_data)
    speed = dist / time
    
    if speed > 900:
        auth = "FRAUD"
    
    return auth

def calcDist(transaction_data, lookup_data):
    geo_map = GEO_Map.get_instance()
    current_lat, current_long = geo_map.get_lat(str(transaction_data['postcode'])).iloc[0], geo_map.get_long(str(transaction_data['postcode'])).iloc[0]
    last_lat, last_long = geo_map.get_lat(str(lookup_data['postcode'])).iloc[0], geo_map.get_long(str(lookup_data['postcode'])).iloc[0]
    dist = geo_map.distance(current_lat, current_long, last_lat, last_long)
    return dist

def calcTime(transaction_data, lookup_data):
    transaction_dt = datetime.strptime(transaction_data['transaction_dt'], '%d-%m-%Y %H:%M:%S')
    time = transaction_dt - lookup_data['transaction_dt']
    hours = time.total_seconds() / 3600
    return hours