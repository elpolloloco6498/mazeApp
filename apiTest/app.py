import pygame
from pygame.locals import *
import requests
import json
from pprint import pprint

# make a simple http request to the maze API
# display graphically the maze
api_endpoint = "http://localhost:5000/"
body = json.dumps({
  "width": 10,
  "height": 10
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", api_endpoint, headers=headers, data=body)
data = response.json()
pprint(data)

# display the data using pygame
WINDOWS_SIZE = (800, 800)
colorCell = (100, 100, 100)
colorEntry = (10, 200, 200)
colorExit = (50, 50, 50)
colorWall = (255, 255, 255)
colorPath = (255, 0, 0)
w = 50
h = 50

def displayCell(cell, color, surface, draw_walls=True):
    # draw rectangle
    x = cell["i"] * w + 200
    y = cell["j"] * h + 200
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(surface, color, rect)
    # draw walls
    if draw_walls:
        walls = cell["walls"]
        if walls["N"]:
            pygame.draw.line(surface, colorWall, [x, y], [x+w, y])
        if walls["W"]:
            pygame.draw.line(surface, colorWall, [x, y], [x, y+h])
        if walls["S"]:
            pygame.draw.line(surface, colorWall, [x, y+h], [x+w, y+h])
        if walls["E"]:
            pygame.draw.line(surface, colorWall, [x+w, y], [x+w, y+h])

def displayMaze(maze, surface):
    for cell in maze["cells"]:
        displayCell(cell, colorCell, surface)
    # display path
    for cell in maze["solve"]:
        displayCell(cell, colorPath, surface)
    # display entry cell
    displayCell(maze["entry"], colorEntry, surface, draw_walls=False)
    # display exit cell
    displayCell(maze["exit"], colorExit, surface, draw_walls=False)

pygame.init()
screen = pygame.display.set_mode(WINDOWS_SIZE)
screen.fill((0, 0, 0))

# display the maze
displayMaze(data, screen)

# event loop pygame
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pygame.display.flip()