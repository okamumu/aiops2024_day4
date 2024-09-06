from pymongo import MongoClient
import paho.mqtt.client as mqtt
import json

# configuration
host = '13.230.249.44' # EC2のIPアドレス
port = 1883
topic = 'sensor'

print("Start subscriber: topic {} on {}:{}".format(topic, host, port))

def on_connect(client, userdata, flags, respons_code):
    print('status {0}'.format(respons_code))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(msg.topic + ' ' + str(msg.payload))
    dbclient = MongoClient('mongodb://mongo:27017/') # コンテナ名 mongo を指定
    db = dbclient['sample']
    collection = db['test']
    doc = json.loads(msg.payload) # JSON形式のデータをPythonの辞書型に変換
    collection.insert_one(doc)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(host, port, 60) # 60 sec keepalive
client.loop_forever()
