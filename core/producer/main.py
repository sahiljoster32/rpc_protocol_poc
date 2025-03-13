from flask import Flask
from celery import Celery
from logger import *

import sys

app = Flask(__name__)
producer = Celery(
    'producer',
    broker='redis://redis:6379/0'
)
producer.conf.task_routes = {
    'tasks.add': {'queue': 'addQueue'},
    'tasks.multiply': {'queue': 'multiplyQueue'}
}

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/produce-add-task')
def produce_add_task():
    producer.send_task('tasks.add', args=[1, 2])
    return 'Task sent!'

@app.route('/produce-mul-task')
def produce_mul_task():
    producer.send_task('tasks.multiply', args=[5, 2])
    return 'Task sent!'

if __name__ == '__main__':
    sys.stdout = sys.stderr = StdFileLogger("producer")
    app.run(host='0.0.0.0', port=8080, debug=True)