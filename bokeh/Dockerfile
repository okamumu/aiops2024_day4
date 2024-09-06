FROM python:3.8

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD [ "bokeh", "serve", "app.py", "--port", "5006", "--allow-websocket-origin=*"]
