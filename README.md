# Real-Time-Credit-Card-Fraud-Detection-Pipeline-
## Credit Card Fraud Detection using Data Engineering Techniques

This project focuses to avoid identity theft, which detects any unusual activity using credit card, which has skyrocketed in the current era. I've used AWS S3 bucket, AWS EMR, Hive, Hadoop, MongoDB, PySpark and Apache Kafka to do this project. I've attached all the necessary files to perform this project in the Media section. Following are the checks performed in my project to detect frauds in Credit Card Transactions:

1. The Transaction would be considered as fraudulent if the Transaction Amount exceeds the Upper Control Limit (UCL) considering the last 10 transactions of the card

2. The Transaction would be considered as fraudulent if the Credit Score is less than 200

3. The geo location of each transaction is captured and the distance and time is identified for them. Considering if the time taken between two transactions does not exceed the speed limit of 900 Km/hr based on the distance, the current transaction would be treated as genuine, if not, as fraudulent.

Following are the steps performed in the project:

1. The Transaction History Data, Card Member Details, Member Score and Zip Code details are uploaded into AWS S3 Bucket
2. A lookup table is created using PySpark over the imported files in MongoDB
3. The lookup table is written back to MongoDB
4. Apache Kafka is used to ingest real-time and the transactions are updated in the Card Transactions Table as fraud or genuine, based on the logic used in the checks
5. If the transaction is genuine, the data is stored in the lookup table and if not, the transaction is not stored and is considered for rejection
