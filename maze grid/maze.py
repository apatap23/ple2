from grid import Grid
from linkedStack import LinkedStack

def getOut (maze, showProcess = False):
    c = choices.pop()
    if maze[c[0][c[1]]] == "G":
        return True
    else:
        maze[c[0]][c[1]] = "."

        if showProcess:
            print(maze)
            input()

        for row, col in [[c[0]+1, c[1],
                        (c[0]-1, c[1]), 
                        (c[0], c[1]+1),
                        (c[0], c[1]-1)]]:
            if row >= 0 and row < maze.getHeight() and \
                col >= 0 and col < maze.getWidth() and \ 
                maze[row][col] not in ".":

                choices.push((row,col))
 
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
