from random import randint

# BACKEND
    # generate maze OK
    # generated maze with custom inputs
    # random maze entry
    # TODO reformat to simplify the code
    # return the maze as a JSON document OK
    # call the maze api and display the maze
    # TODO write unittest for backend

# FRONTEND
    # TODO set up the angular app
    # TODO call the maze api and display the raw data
    # TODO using the d3.js module display the maze graphically
    # TODO add a form to send additional data to the API

class Grid:
    def __init__(self, cols, rows):
        self.rows = rows
        self.cols = cols
        self.cells = []

        for j in range(rows):
            for i in range(cols):
                self.cells.append(Cell(i, j))

    def index(self, i, j):
        if i < 0 or i > self.cols-1 or j < 0 or j > self.rows-1:
            return -1
        return j*self.cols + i

    def indexCell(self, cell):
        return self.index(cell.i, cell.j)

class Maze(Grid):
    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.entry = self.entryCell()
        self.entry.visited = True
        self.entry.removeNorth()
        self.exit = self.exitCell()
        self.exit.removeSouth()
        self.solve = []

    def entryCell(self):
        index = self.index(self.cols//2, 0)
        return self.cells[index]

    def exitCell(self):
        index = self.index(self.cols // 2, self.rows - 1)
        return self.cells[index]

    def cellOnBorder(self, cell):
        i, j = cell.i, cell.j
        return (j == 0 or j == self.rows-1) or (i == 0 or i == self.cols-1)

    """def initMazeEntry(self):
        # the entry of the maze is on the border
        border_cells = list(filter(self.cellOnBorder, self.cells))
        cell = border_cells[randint(0, len(border_cells)-1)]
        cell.visited = True
        # delete entry wall
        possible_entry_walls = []
        if cell.i == 0:
            possible_entry_walls.append("W")
        if cell.i == self.cols-1:
            possible_entry_walls.append("E")
        if cell.j == 0:
            possible_entry_walls.append("N")
        if cell.j == self.rows - 1:
            possible_entry_walls.append("S")

        randnb = 0 if len(possible_entry_walls) == 0 else randint(0, len(possible_entry_walls)-1)
        wall_to_delete = possible_entry_walls[randnb]
        if wall_to_delete == "N":
            cell.walls[0] = False
        if wall_to_delete == "W":
            cell.walls[1] = False
        if wall_to_delete == "S":
            cell.walls[2] = False
        if wall_to_delete == "E":
            cell.walls[3] = False
        # update data structure
        self.visited += 1
        self.stack.append(cell)"""

    def removeWall(self, cellA, cellB):
        x = cellA.i - cellB.i
        if x == 1: # cell b on the left
            cellA.removeWest() # delete west wall
            cellB.removeEast() # delete east wall
        elif x == -1: # cell b on the right
            cellA.removeEast() # delete east wall
            cellB.removeWest() # delete west wall

        y = cellA.j - cellB.j
        if y == 1:  # cell b on the top
            cellA.removeNorth() # delete northern wall
            cellB.removeSouth() # delete southern wall
        elif y == -1:  # cell b on the bottom
            cellA.removeSouth() # delete southern wall
            cellB.removeNorth() # delete northern wall

    def getAdjacents(self, cell):
        adjacents = []
        i, j = cell.i, cell.j
        indexAdjacents = [self.index(i, j-1), self.index(i-1, j), self.index(i, j+1), self.index(i+1, j)]
        for id in indexAdjacents:
            if id != -1:
                adjacents.append(self.cells[id])
        return adjacents

    def getAdjacentsNotVisited(self, cell):
        adjacents = self.getAdjacents(cell)
        return [cell for cell in adjacents if not cell.visited]

    def getRandAdjacentNotVisited(self, cell):
        adjacents = self.getAdjacentsNotVisited(cell)
        if adjacents:
            return adjacents[randint(0, len(adjacents)-1)]
        else:
             return None

    def generateMaze(self):
        stack = list()
        stack.append(self.entry)
        visited = 1
        while stack:
            current = stack[-1] # get last cell on the stack
            adjacentCell = self.getRandAdjacentNotVisited(current)
            if adjacentCell:
                self.removeWall(current, adjacentCell) # remove wall between old cell and new cell
                adjacentCell.visited = True # mark the cell as visited
                stack.append(adjacentCell) # add the cell to the stack
                if adjacentCell == self.exit and not self.solve: # when we found the exit we remember the path
                    print("path found !")
                    self.solve = stack.copy()
                visited += 1
            else: # backtrack in the stack
                stack.pop(-1) # removes the last element of the stack that doesn't have adjacent cells

    def toJSON(self):
        listFormattedCells = []
        mazeData = {
            "cols": self.cols,
            "rows": self.rows,
            "entry": self.entry.toJSON(),
            "exit": self.exit.toJSON(),
            "solve": [cell.toJSON() for cell in self.solve],
            "cells": [cell.toJSON() for cell in self.cells]
        }
        return mazeData

class Cell:
    def __init__(self, i, j):
        # i : column index coordinate of the cell
        # j: row index coordinate of the cell
        self.i = i
        self.j = j
        # walls : [north, west, south, east]
        self.walls = [1, 1, 1, 1]
        self.visited = False

    def __repr__(self):
        return f"({self.i}, {self.j})\n"\
        f"north:{self.northWall} west:{self.westWall} south:{self.southWall} east:{self.eastWall}\n"

    def toJSON(self):
        return {
            "i": self.i,
            "j": self.j,
            "walls": {
                "N": self.northWall,
                "W": self.westWall,
                "S": self.southWall,
                "E": self.eastWall
            }
        }

    @property
    def northWall(self):
        return self.walls[0]
    @property
    def westWall(self):
        return self.walls[1]
    @property
    def southWall(self):
        return self.walls[2]
    @property
    def eastWall(self):
        return self.walls[3]

    def removeNorth(self):
        self.walls[0] = 0
    def removeWest(self):
        self.walls[1] = 0
    def removeSouth(self):
        self.walls[2] = 0
    def removeEast(self):
        self.walls[3] = 0

    # TODO creates setters for walls