import json
from time import time
from random import random
from flask import Flask, render_template, make_response

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', data='test')

@app.route('/live-data')
def live_data():
    # Create a PHP array and echo it as JSON
    process = psutil.Process(os.getpid())
    mem = process.get_memory_info()[0] / float(2 ** 20)
    return mem


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
