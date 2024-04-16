from flask import Flask, redirect, url_for
from prometheus_client import Summary
import json
from datetime import datetime
import time
import random

app = Flask(__name__)

@app.route('/')
def index():
    return '<H1>Hello from Test Docker Image</H1>'

@app.route('/sleep/<int:seconds>')
def sleep(seconds:int):
    getdatetimenow = lambda : str(datetime.now())
    result = {'start_time':getdatetimenow()}
    time.sleep(seconds)
    result['end_time'] = str(getdatetimenow())
    result['slept_for'] = seconds
    return json.dumps(result)

@app.route('/sleep/random')
def sleep_random():
    random_sleep_seconds = random.randint(0,4)
    return redirect(url_for('sleep',seconds=random_sleep_seconds))

def main():
    app.run(debug=True,port=3000)

if __name__ == '__main__':
    main()
