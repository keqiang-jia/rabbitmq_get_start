import threading

from flask import Flask

from receive import receive

app = Flask(__name__)

thread = threading.Thread(target=receive)
thread.daemon = True
thread.start()


@app.route("/")
def hello_world():
    return "<p>Hello, World</p>"
