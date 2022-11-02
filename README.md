# mazeApp
Maze app is a simple angular web application.

## Description of the project
The goal of this project is to do something similar to https://www.mazegenerator.net but in a simpler version.\
The maze has to be generated on a backend server. We will use an api to make the frontend and backend part communicate.\
I have use AngularJs for the frontend of the application and Flask for the backend.\
The maze is displayed using D3.js which is a data driven visualizer. I used it to display the cells of the maze

The behavior is simple, the frontend will send an api request to the backend server which will generate a maze and return a json document containing the necessary information for plotting the maze in d3.js\

The json format returned by the api is the following:\
This is an example for width=4 and height=4\
```
{
    "cells": [
        {
            "i": 0,
            "j": 0,
            "walls": {
                "E": 0,
                "N": 1,
                "S": 0,
                "W": 1
            }
        },
        {
            "i": 1,
            "j": 0,
            "walls": {
                "E": 1,
                "N": 1,
                "S": 1,
                "W": 0
            }
        },
        {
            "i": 2,
            "j": 0,
            "walls": {
                "E": 1,
                "N": 0,
                "S": 0,
                "W": 1
            }
        },
        {
            "i": 3,
            "j": 0,
            "walls": {
                "E": 1,
                "N": 1,
                "S": 0,
                "W": 1
            }
        },
        {
            "i": 0,
            "j": 1,
            "walls": {
                "E": 0,
                "N": 0,
                "S": 0,
                "W": 1
            }
        },
        {
            "i": 1,
            "j": 1,
            "walls": {
                "E": 1,
                "N": 1,
                "S": 0,
                "W": 0
            }
        },
        {
            "i": 2,
            "j": 1,
            "walls": {
                "E": 1,
                "N": 0,
                "S": 0,
                "W": 1
            }
        },
        {
            "i": 3,
            "j": 1,
            "walls": {
                "E": 1,
                "N": 0,
                "S": 0,
                "W": 1
            }
        },
        {
            "i": 0,
            "j": 2,
            "walls": {
                "E": 1,
                "N": 0,
                "S": 0,
                "W": 1
            }
        },
        {
            "i": 1,
            "j": 2,
            "walls": {
                "E": 0,
                "N": 0,
                "S": 1,
                "W": 1
            }
        },
        {
            "i": 2,
            "j": 2,
            "walls": {
                "E": 1,
                "N": 0,
                "S": 1,
                "W": 0
            }
        },
        {
            "i": 3,
            "j": 2,
            "walls": {
                "E": 1,
                "N": 0,
                "S": 0,
                "W": 1
            }
        },
        {
            "i": 0,
            "j": 3,
            "walls": {
                "E": 0,
                "N": 0,
                "S": 1,
                "W": 1
            }
        },
        {
            "i": 1,
            "j": 3,
            "walls": {
                "E": 0,
                "N": 1,
                "S": 1,
                "W": 0
            }
        },
        {
            "i": 2,
            "j": 3,
            "walls": {
                "E": 0,
                "N": 1,
                "S": 0,
                "W": 0
            }
        },
        {
            "i": 3,
            "j": 3,
            "walls": {
                "E": 1,
                "N": 0,
                "S": 1,
                "W": 0
            }
        }
    ],
    "cols": 4,
    "entry": {
        "i": 2,
        "j": 0,
        "walls": {
            "E": 1,
            "N": 0,
            "S": 0,
            "W": 1
        }
    },
    "exit": {
        "i": 2,
        "j": 3,
        "walls": {
            "E": 0,
            "N": 1,
            "S": 0,
            "W": 0
        }
    },
    "rows": 4,
    "solve": [
        {
            "i": 2,
            "j": 0,
            "walls": {
                "E": 1,
                "N": 0,
                "S": 0,
                "W": 1
            }
        },
        {
            "i": 2,
            "j": 1,
            "walls": {
                "E": 1,
                "N": 0,
                "S": 0,
                "W": 1
            }
        },
        {
            "i": 2,
            "j": 2,
            "walls": {
                "E": 1,
                "N": 0,
                "S": 1,
                "W": 0
            }
        },
        {
            "i": 1,
            "j": 2,
            "walls": {
                "E": 0,
                "N": 0,
                "S": 1,
                "W": 1
            }
        },
        {
            "i": 1,
            "j": 1,
            "walls": {
                "E": 1,
                "N": 1,
                "S": 0,
                "W": 0
            }
        },
        {
            "i": 0,
            "j": 1,
            "walls": {
                "E": 0,
                "N": 0,
                "S": 0,
                "W": 1
            }
        },
        {
            "i": 0,
            "j": 2,
            "walls": {
                "E": 1,
                "N": 0,
                "S": 0,
                "W": 1
            }
        },
        {
            "i": 0,
            "j": 3,
            "walls": {
                "E": 0,
                "N": 0,
                "S": 1,
                "W": 1
            }
        },
        {
            "i": 1,
            "j": 3,
            "walls": {
                "E": 0,
                "N": 1,
                "S": 1,
                "W": 0
            }
        },
        {
            "i": 2,
            "j": 3,
            "walls": {
                "E": 0,
                "N": 1,
                "S": 0,
                "W": 0
            }
        }
    ]
}
```

## Setup of the application``
Start by cloning the project in a directory that you see fit.\
```
git clone https://github.com/elpolloloco6498/mazeApp.git
```
Once that is done you have access to two files: mazeFrontend & mazeBackend.\
### Setup the frontend
Navigate to the frontend folder
```
cd mazeApp
cd ./mazeFrontend
```
You need to install all the necessary dependencies.\
Make sure npm is installed on your machine.\
```
npm install
```
To run the program execute the following command\
```
npm start
```
### Setup the backend
Now that the frontend is ready we need to setup the backend.\
```
cd ../mazeBackend
```
You will need Python 3.x to run this program.\
Install the following dependencies:\
```
pip install flask, flask_cors
```
To start the server in developement mode type:\
```
python -m flask --app mazeApi run
```

The API is now available at : http://localhost:5000

Access the web application at : http://localhost:4200 and try to generate a maze.

## Algorithm
The algorithm that is used to generate the maze is simple and based on DFS (Depth First Search). The data structure that is being used here is the stack.
The generation of the solution of the maze is generated while generating the maze.

## Improvements
I used a simple algorithm to generate the maze. However this is not the most efficient method there are better algorithms out there that could help generate bigger maze in less time.
