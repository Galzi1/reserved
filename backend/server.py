from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient()
db = client.reserves
reservists = db.reservists

@app.route('/')
def hello():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)