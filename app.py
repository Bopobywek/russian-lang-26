import random
import json

from flask import Flask, render_template, session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'filesystem'
with open("tasks.json") as fin:
       data = json.loads(fin.read())


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/task/<string:last>/", methods=["GET"])
def get_new_task(last):
    tasks = session.get("tasks", None)
    if tasks is not None and (tasks.index(last) + 1) != len(tasks):
        ch = tasks[tasks.index(last) + 1]
        print(tasks.index(last), len(tasks))
    else:
        tasks = list(data.keys())
        random.shuffle(tasks)
        ch = tasks[0]
        session["tasks"] = tasks
    return json.dumps({"task_id": int(ch), "question": list(data[ch].keys())[0].capitalize(), "answer": list(data[ch].values())[0]})

