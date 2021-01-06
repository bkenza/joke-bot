from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def home():
    return "Hello, I am the joke bot & I am alive!"


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    th = Thread(target=run)
    th.start()
