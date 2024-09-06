from pymongo import MongoClient

# 以下と同じ操作を行う
# use sample
# db.test.insertOne({name: "Alice"})
# db.test.insertOne({name: "Bob", age: 31})
# db.test.find()

client = MongoClient('mongodb://localhost:27017/')
db = client['sample']
collection = db['test']

cursor = collection.find({'location': 'room 1'}).sort('timestamp', -1).limit(10)
# for doc in cursor:
#     print(doc['temperature'])

y1 = [doc['temperature'] for doc in cursor]

