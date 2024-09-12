import sys
sys.path.append("..")
from db.geo_map import GEO_Map
from db.dao import *
from datetime import datetime

# Read the transaction data from the lookup table in MongoDB
collection_lookup = readMongoLookup()