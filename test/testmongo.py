from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['sample']
collection = db['test']

cursor = collection.find({'location': 'room 1'}).sort('timestamp', -1).limit(100)
documents = list(cursor)
documents.reverse()
x = [float(doc['timestamp']) for doc in documents]
y1 = [doc['temperature'] for doc in documents]
y2 = [doc['humidity'] for doc in documents]
print(x)
print(y1)
print(y2)
