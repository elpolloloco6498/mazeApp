from flask import Flask, jsonify
from maze import *
app = Flask(__name__)

@app.route('/')
def generatedMaze():
    maze = Maze(5,4)
    maze.generateMaze()
    mazeData = maze.toJSON()
    return jsonify(mazeData)
