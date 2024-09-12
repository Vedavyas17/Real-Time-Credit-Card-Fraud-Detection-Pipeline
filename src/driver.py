from rules.rules import processMessage
from db.dao import *

if __name__ == "__main__":
    # Read data from Kafka Topic
    consumer = readKafka()