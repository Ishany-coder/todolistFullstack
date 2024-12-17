from flask import Flask, jsonify
from main import add_task, remove_task, show_list
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={
    r"/*": {
        "origins": [
            "http://localhost:5173",
            "http://127.0.0.1:5173"
        ],
        "methods": ["GET", "POST", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

@app.route('/add/<task>')
def add(task):
    todoList = add_task(task)
    return jsonify({
        "message": "Task added successfully",
        "task": task,
        "todoList": todoList
    })

@app.route('/show')
def show():
    todoList = show_list()
    return jsonify({
        "todoList": todoList
    })

@app.route('/remove/<task>', methods=['DELETE'])
def remove(task):
    todoList = remove_task(task)
    return jsonify({
        "message": "Task removed successfully",
        "task": task,
        "todoList": todoList
    })

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)