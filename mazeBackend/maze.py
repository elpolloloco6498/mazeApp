from random import randint

# BACKEND
    # generate maze OK
    # TODO generated maze with custom inputs
    # TODO random maze entry
    # TODO reformat to simplify the code
    # return the maze as a JSON document OK
    # TODO call the maze api and display the maze
    # TODO write unittest for backend

# FRONTEND
    # TODO set up the angular app
    # TODO call the maze api and display the raw data
    # TODO using the d3.js module display the maze graphically
    # TODO add a form to send additional data to the API

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = []

        for j in range(rows):
            for i in range(cols):
                self.cells.append(Cell(i, j))

    def index(self, i, j):
        if (i < 0 or i > self.cols-1 or j < 0 or j > self.rows-1):
            return -1
        return j*self.cols + i

    def indexCell(self, cell):
        return self.index(cell.i, cell.j)

class Maze(Grid):
    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        # TODO choose a random starting cell on the edge
        # for now we use the top left corner
        self.stack = [self.cells[0]] # for backtracking
        self.visited = 1 # contains visited cell of the maze
        self.cells[0].visited = True

    @property
    def allCellsVisited(self):
        return self.visited == len(self.cells)

    def removeWall(self, cellA, cellB):
        x = cellA.i - cellB.i
        if x == 1: # cell b on the left
            cellA.walls[1] = False # delete west wall
            cellB.walls[3] = False # delete east wall
        elif x == -1: # cell b on the right
            cellA.walls[3] = False # delete east wall
            cellB.walls[1] = False # delete west wall

        y = cellA.j - cellB.j
        if y == 1:  # cell b on the top
            cellA.walls[0] = False # delete northern wall
            cellB.walls[2] = False # delete southern wall
        elif y == -1:  # cell b on the bottom
            cellA.walls[2] = False # delete southern wall
            cellB.walls[0] = False # delete northern wall

    def getAdjacents(self, cell):
        adjacents = []
        i, j = cell.i, cell.j
        indexAdjacents = [self.index(i, j-1), self.index(i-1, j), self.index(i, j+1), self.index(i+1, j)]
        for id in indexAdjacents:
            if id != -1:
                adjacents.append(id)
        return adjacents

    def getAdjacentsNotVisited(self, cell):
        adjacents = self.getAdjacents(cell)
        return [id for id in adjacents if not self.cells[id].visited]

    def generateMaze(self):
        while self.stack != [] and not self.allCellsVisited:
            parentCell = self.stack[-1] # get last cell on the stack
            adjancentCells = self.getAdjacentsNotVisited(parentCell)
            if adjancentCells:
                cellId = adjancentCells[randint(0, len(adjancentCells)-1)]
                currentCell = self.cells[cellId]
                # remove wall between old cell and new cell
                self.removeWall(self.cells[self.indexCell(parentCell)], self.cells[cellId])
                # mark the cell as visited
                self.cells[cellId].visited = True
                # add the cell to the stack
                self.stack.append(self.cells[cellId])
                self.visited += 1
            else: # backtrack in the stack
                currentCell = self.stack.pop(-1) # removes the last element of the stack that doesn't have adjacent cells

    def toJSON(self):
        listFormattedCells = []
        mazeData = {
            "cols": self.cols,
            "rows": self.rows,
        }
        for cell in self.cells:
            listFormattedCells.append({
                "i": cell.i,
                "j": cell.j,
                "walls": {
                    "north": cell.northWall,
                    "west": cell.westWall,
                    "south": cell.southWall,
                    "east": cell.eastWall
                }
            })
        mazeData["cells"] = listFormattedCells
        return mazeData

class Cell:
    def __init__(self, i, j):
        # i : column index coordinate of the cell
        # j: row index coordinate of the cell
        self.i = i
        self.j = j
        # walls : [north, west, south, east]
        self.walls = [True, True, True, True]
        self.visited = False

    def __repr__(self):
        return f"({self.i}, {self.j})\n"\
        f"north:{self.northWall} west:{self.westWall} south:{self.southWall} east:{self.eastWall}\n"

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