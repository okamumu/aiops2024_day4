from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource
from bokeh.layouts import column, row
import numpy as np
import random
import time
from pymongo import MongoClient

# データソースの作成
xdata = []
y1data = []
y2data = []
source1 = ColumnDataSource(data=dict(x=[], y=[]))
source2 = ColumnDataSource(data=dict(x=[], y=[]))

# グラフの作成
plot1 = figure(title="Temprature", x_axis_label='time', y_axis_label='y1')
plot1.line('x', 'y', source=source1)

plot2 = figure(title="Humidity", x_axis_label='time', y_axis_label='y2')
plot2.line('x', 'y', source=source2)

# データの更新関数
def update():
  # データの追加．100個以上ある場合は古いデータを削除
  if len(xdata) > 100:
    xdata.pop(0)
    y1data.pop(0)
    y2data.pop(0)
  xdata.append(time.time())
  y1data.append(random.random())
  y2data.append(random.random())
  source1.data = dict(x=xdata, y=y1data)
  source2.data = dict(x=xdata, y=y2data)

# Bokehのドキュメントにコールバックを追加（1000ミリ秒ごとに更新）
curdoc().add_periodic_callback(update, 1000)

# レイアウトの設定
layout = row(plot1, plot2)
curdoc().add_root(layout)
curdoc().title = "Temprature and Humidity"
