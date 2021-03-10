from flask import Flask,jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'Name': u'Raju',
        'Number': u'5676546548', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'Jolie',
        'Number': u'6854168698', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hello"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['title'],
        'Number': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)
