#Lists

#maze = [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [1, 0, 0, 1, 1], [1, 1, 1, 0, 1]]
maze = [[1, 1, 0, 0, 0, 0], 
        [1, 0, 1, 1, 1, 1], 
        [1, 0, 1, 0, 0, 1], 
        [1, 0, 1, 1, 0, 1], 
        [1, 0, 0, 1, 0, 1], 
        [1, 1, 1, 1, 0, 1] ]

'''maze = [ [ 1, 0, 0, 0, 0 ],
          [ 1, 1, 1, 1, 1 ],
          [ 1, 1, 1, 0, 1 ],
          [ 0, 0, 0, 0, 1 ],
          [ 0, 0, 0, 0, 1 ] ]'''

solution = [[0 for i in range (6)] for item in range (6)]
def print_maze(maze):
    for item in maze:
        print(item)

print_maze(maze)
print('\n')

def isSafe(maze, x, y, solution):
    if x<len(maze) and y<len(maze) and maze[x][y]==1 and x>-1 and y>-1 and solution[x][y]==0:
        return True
    
    return False

def ratInMaze(maze, x, y, solution):
    if maze[len(maze)-1][len(maze)-1]!= 1:
        return False
    
    if x==len(maze)-1 and y==len(maze)-1:
        solution[x][y]=1
        return True

    if isSafe(maze, x, y, solution):
        solution[x][y]=1

        if ratInMaze(maze, x, y+1, solution):
            return True
        
        if ratInMaze(maze, x-1, y, solution):
            return True

        if ratInMaze(maze, x+1, y, solution):
            return True

        if ratInMaze(maze, x, y-1, solution):
            return True
    
        solution[x][y]=0
        return False
    
    return False

ratInMaze(maze, 0, 0, solution)

print_maze(solution)


