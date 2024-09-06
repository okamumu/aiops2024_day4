from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource
from bokeh.layouts import column, row
import numpy as np
import random
import time
from pymongo import MongoClient

client = MongoClient('mongodb://mongo:27017/')
db = client['sample']
collection = db['test']

# データソースの作成
source1 = ColumnDataSource(data=dict(x=[], y=[]))
source2 = ColumnDataSource(data=dict(x=[], y=[]))

# グラフの作成
plot1 = figure(title="Temprature", x_axis_label='time', y_axis_label='y1')
plot1.line('x', 'y', source=source1)

plot2 = figure(title="Humidity", x_axis_label='time', y_axis_label='y2')
plot2.line('x', 'y', source=source2)

# データの更新関数
def update():
  cursor = collection.find({'location': 'room 1'}).sort('timestamp', -1).limit(100)
  documents = list(cursor)
  documents.reverse()
  x = [float(doc['timestamp']) for doc in documents]
  y1 = [doc['temperature'] for doc in documents]
  y2 = [doc['humidity'] for doc in documents]
  source1.data = dict(x=x, y=y1)
  source2.data = dict(x=x, y=y2)

# Bokehのドキュメントにコールバックを追加（1000ミリ秒ごとに更新）
curdoc().add_periodic_callback(update, 1000)

# レイアウトの設定
layout = row(plot1, plot2)
curdoc().add_root(layout)
curdoc().title = "Temprature and Humidity"
