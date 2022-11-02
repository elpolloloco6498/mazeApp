from flask import Flask, jsonify, request
from flask_cors import CORS
from maze import *
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def generatedMaze():
    # get data from the body
    request_data = request.get_json()
    width = request_data["width"]
    height = request_data["height"]

    maze = Maze(width, height)
    maze.generateMaze()
    maze_data = maze.toJSON()
    return jsonify(maze_data)
