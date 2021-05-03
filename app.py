import random
import json

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/task/<string:last>/", methods=["GET"])
def get_new_task(last):
    with open("tasks.json") as fin:
       data = json.loads(fin.read())

    ch = random.choice(list(data.keys()))
    while ch == last:
        ch = random.choice(list(data.keys()))
    return json.dumps({"task_id": int(ch), "question": list(data[ch].keys())[0].capitalize(), "answer": list(data[ch].values())[0]})

