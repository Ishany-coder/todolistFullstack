from flask import Flask, jsonify
from main import add_task, remove_task, show_list
from flask_cors import CORS

app = Flask(__name__)

# Updated CORS configuration to handle both localhost and 127.0.0.1
CORS(app, origins="*")

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

if __name__ == '__main__':
    # Be explicit about the host and port
    app.run(host='127.0.0.1', port=5000, debug=True)