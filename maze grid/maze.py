from grid import Grid
from linkedStack import LinkedStack

def getOut (maze, showProcess = False):
    pass

def getMazeFromFile():
    fileObj = open("maze1.txt", "r")
    firstLine = list(map(int, fileObj).readline().strip().split()))

    rows = firstline[0]
    columns = firstLine [1]

    maze = Grid(rows, columns,"*")

    for row in range(rows):
        line = fileObj.readline().strip()

        for col in range(columns):
            maze[row][col] = line[col]

    return maze

def findStartPs(maze):
    for row in range(maze.getHeight()):
        for column in range(maze.getWidth()):
            if maze[row][column] == "S":
                return [row, column]
