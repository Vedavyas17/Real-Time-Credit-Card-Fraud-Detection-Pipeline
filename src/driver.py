from rules.rules import processMessage
from db.dao import *

if __name__ == "__main__":
    # Read data from Kafka Topic
    consumer = readKafka()
    
    # Loop through Kafka messages
    for message in consumer:
        # Get actual message
        currentMessage = message.value
        
        # Determine if the transaction is fraudulent or not
        status = processMessage(currentMessage)
        
        # Add status to the message
        currentMessage["status"] = status
        
        # Print the current message status
        print(currentMessage)
        
        # Write the message to MongoDB
        writeToMongo(currentMessage)