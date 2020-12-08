#Backtracking Algorithm - Sudoku Solver - www.101computing.net/backtracking-algorithm-sudoku-solver/
import turtle
from random import randint
from time import sleep

myPen = turtle.Turtle()
topLeft_x=-150
topLeft_y=150


def text(message,x,y,size):
    FONT = ('Arial', size, 'normal')
    myPen.penup()
    myPen.goto(x,y)    		  
    myPen.write(message,align="left",font=FONT)

#A procedure to draw the grid on screen using Python Turtle
def drawGrid(grid,walk):
  intDim=35
  for row in range(0,10):
    if (row%3)==0:
      myPen.pensize(3)
    else:
      myPen.pensize(1)
    myPen.penup()
    myPen.goto(topLeft_x,topLeft_y-row*intDim)
    myPen.pendown()
    myPen.goto(topLeft_x+9*intDim,topLeft_y-row*intDim)
  for col in range(0,10):
    if (col%3)==0:
      myPen.pensize(3)
    else:
      myPen.pensize(1)    
    myPen.penup()
    myPen.goto(topLeft_x+col*intDim,topLeft_y)
    myPen.pendown()
    myPen.goto(topLeft_x+col*intDim,topLeft_y-9*intDim)

  for row in range (0,9):
      for col in range (0,9):
        if (walk):
            if((row,col) in walk):
                myPen.pencolor("red")
            else :
                myPen.pencolor("black")
        if grid[row][col]!=0:
          text(grid[row][col],topLeft_x+col*intDim+9,topLeft_y-row*intDim-intDim+8,18)

def getPalendrome(grid,walk):
    values = []
    for pos in walk:
        values.append(grid[pos[0]][pos[1]])
    return values

def isPalendrome(grid,walk):
    values = getPalendrome(grid,walk)
    rlist = values.copy()
    rlist.reverse()
    return rlist == values

def checkPalendromeWalk(grid,walk):
    # the final walk position must be 7,1
    if (walk[-1] != (7,1)):
        return False

    #print("Walk of length %d found to reach (7,1)"%(len(walk)))
    #print(walk)

    # the walk must be a palindrome
    if (isPalendrome(grid,walk)):
        return True

    return False

def isValidSnake(walk,step):
    # not valid if step is already in snake
    if ( step in walk ):
        return False # do not re-walk path

    notValid = [(1,3),(2,8),(3,1),(5,5),(5,6),(6,1),(6,2),(6,7),(8,0),(8,1),(8,3)]

    if ( step in notValid ):
        return False # do not re-walk path
    # not valid if with 

    # ignoring the last 2 steps, you may not be adjacent to a position.
    if (len(walk) > 2):
        shorterWalk = walk[:-2]
        # generate the 8 postions 1 step away
        for rd in [-1,0,1]:
            for cd in [-1,0,1]:
                t = (step[0]+rd,step[1]+cd)
                if (t in shorterWalk):
                    return False

    return True

def walkNorthAndRecurse(grid,walk):
    # add north to walk if valid
    lastWalkPosition = walk[-1] #row,column
    if (lastWalkPosition[0] > 0): # of row is greater than one, we can go north
        row = lastWalkPosition[0] - 1
        col = lastWalkPosition[1]

        if (False == isValidSnake(walk,(row,col))):
            return False # do not re-walk path

        walk.append((row,col))
        if checkPalendromeWalk(grid,walk) :
            print("Walk Complete and Checked")
            return True
        else:
            if (False == solvePalendromeWalk(grid,walk)):
                walk.pop()
                #back track walk
    else:
        return False # invalid step off of grid
    
    return False # this was a mistep

def walkSouthAndRecurse(grid,walk):
    # add south to walk if valid
    lastWalkPosition = walk[-1] #row,column
    if (lastWalkPosition[0] < 8):
        row = lastWalkPosition[0] + 1
        col = lastWalkPosition[1]

        if (False == isValidSnake(walk,(row,col))):
            return False # do not re-walk path

        walk.append((row,col))
        if checkPalendromeWalk(grid,walk) :
            print("Walk Complete and Checked")
            return True
        else:
            if (False == solvePalendromeWalk(grid,walk)):
                walk.pop()
                #back track walk
    else:
        return False # invalid step off of grid
    
    return False # this was a mistep

def walkEastAndRecurse(grid,walk):

    lastWalkPosition = walk[-1] #row,column
    if (lastWalkPosition[1] < 8):
        row = lastWalkPosition[0]
        col = lastWalkPosition[1] + 1
        
        if (False == isValidSnake(walk,(row,col))):
            return False # do not re-walk path

        walk.append((row,col))
        if checkPalendromeWalk(grid,walk) :
            print("Walk Complete and Checked")
            return True
        else:
            if (False == solvePalendromeWalk(grid,walk)):
                walk.pop()
                #back track walk
    else:
        return False # invalid step off of grid
    
    return False # this was a mistep

def walkWestAndRecurse(grid,walk):

    lastWalkPosition = walk[-1] #row,column
    if (lastWalkPosition[1] > 0):
        row = lastWalkPosition[0]
        col = lastWalkPosition[1] - 1

        if (False == isValidSnake(walk,(row,col))):
            return False # do not re-walk path

        walk.append((row,col))
        if checkPalendromeWalk(grid,walk) :
            print("Walk Complete and Checked")
            return True
        else:
            if (False == solvePalendromeWalk(grid,walk)):
                walk.pop()
                #back track walk
    else:
        return False # invalid step off of grid
    
    return False # this was a mistep

def isGridCellOnWalkAlready(walk,gridCell):
    for p in walk:
      if p[0] == gridCell:
        return True
      if p[1] == gridCell:
        return True
    return False

def isGridCellOnGrid(gridCell):
  (row,col) = gridCell
  if (row > 8 or row < 0 ):
    return False
  if (col > 8 or col < 0 ):
    return False
  return True

def isGreyCell(gridCell):
    notValid = [(1,3),(2,8),(3,1),(5,5),(5,6),(6,1),(6,2),(6,7),(8,0),(8,1),(8,3)]
    for p in notValid:
      if p == gridCell:
        return True
    return False

def canUseGridCell(gridCell,walk):
  if isGridCellOnGrid(gridCell):
    if not isGreyCell(gridCell):
      if not isGridCellOnWalkAlready(walk,gridCell):
        return True
  return False

def gridValue(grid,gridCell):
  (row,col) = gridCell
  return grid[row][col]

def checkSnake(grid,walk):
  # For a position on walk
  # only the next position and the previous position may be within 1 square

  # For each grey square, count the number of snake tiles in the surrounding 8 squares
  # this should equal the value in the grey square
  return True

def solvePalendromeWalk(grid,walk):
    
    #myPen.clear()
    #drawGrid(grid,walk) 
    #myPen.getscreen().update()

    # the current end tuple is two values on the grid
    (snakeA,snakeB) = walk[-1]

    if (snakeA == snakeB): # The two ends have met
      return checkSnake(grid,walk)

    # There are 4 positions around snakeA and 4 positions around snakeB
    for r1 in [-1,0,1]:
      for c1 in [-1,0,1]:
        # don't allow the diagonals
        if (abs(r1) + abs(c1) < 2):
          for r2 in [-1,0,1]:
            for c2 in [-1,0,1]:
              # don't allow the diagonals
              if (abs(r2) + abs(c2) < 2):
                nextSnakeA = (snakeA[0]+r1,snakeA[1]+c1)
                nextSnakeB = (snakeB[0]+r2,snakeB[1]+c2)
                if (canUseGridCell(nextSnakeA,walk) and canUseGridCell(nextSnakeB,walk)):
                  gridCellA = gridValue(grid,nextSnakeA)
                  gridCellB = gridValue(grid,nextSnakeB)
                  if (gridCellA == gridCellB):
                    walk.append((nextSnakeA,nextSnakeB))
                    if not solvePalendromeWalk(grid,walk):
                      walk.pop(-1)

    return False

#A function to check if the grid is full
def checkGrid(grid):
  for row in range(0,9):
      for col in range(0,9):
        if grid[row][col]==0:
          return False

  
  # must start and end of the same
  if (grid[4][0] != grid[7][1]):
      return False

  print("Suduku solution - looking for snake")

  # Testing walk 
  walk = []
  #myPen.clear()
  #drawGrid(grid,walk) 
  #myPen.getscreen().update()

  walk.append(((4,0),(7,1)))

  if (solvePalendromeWalk(grid,walk)):
    myPen.clear()
    drawGrid(grid,walk) 
    myPen.getscreen().update()
    return True

  return False

  #return True 




#A backtracking/recursive function to check all possible combinations of numbers until a solution is found
def solveGrid(grid):
  #Find next empty cell
  for i in range(0,81):
    row=i//9
    col=i%9
    if grid[row][col]==0:
      for value in range (1,10):
        #Check that this value has not already be used on this row
        if not(value in grid[row]):
          #Check that this value has not already be used on this column
          if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
            #Identify which of the 9 squares we are working on
            square=[]
            if row<3:
              if col<3:
                square=[grid[i][0:3] for i in range(0,3)]
              elif col<6:
                square=[grid[i][3:6] for i in range(0,3)]
              else:  
                square=[grid[i][6:9] for i in range(0,3)]
            elif row<6:
              if col<3:
                square=[grid[i][0:3] for i in range(3,6)]
              elif col<6:
                square=[grid[i][3:6] for i in range(3,6)]
              else:  
                square=[grid[i][6:9] for i in range(3,6)]
            else:
              if col<3:
                square=[grid[i][0:3] for i in range(6,9)]
              elif col<6:
                square=[grid[i][3:6] for i in range(6,9)]
              else:  
                square=[grid[i][6:9] for i in range(6,9)]
            #Check that this value has not already be used on this 3x3 square
            if not value in (square[0] + square[1] + square[2]):
              grid[row][col]=value
              #myPen.clear()
              #drawGrid(grid) 
              #myPen.getscreen().update()            
              if checkGrid(grid):
                print("Grid Complete and Checked")
                return True
              else:
                if solveGrid(grid):
                  return True
      break
  #print("Backtrack")
  grid[row][col]=0  
  
  

def mainTask():
  #initialise empty 9 by 9 grid
  grid = []
  grid.append([5, 0, 0, 3, 0, 0, 0, 0, 0])
  grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
  grid.append([7, 0, 0, 0, 0, 0, 0, 0, 0])
  grid.append([0, 0, 0, 0, 0, 8, 0, 0, 0])
  grid.append([0, 0, 1, 0, 0, 0, 2, 0, 0])
  grid.append([0, 0, 0, 5, 0, 0, 0, 0, 0])
  grid.append([0, 0, 0, 0, 0, 0, 0, 0, 3])
  grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
  grid.append([0, 0, 0, 0, 0, 3, 0, 0, 9])

  turtle.tracer(0)
  #myPen.tracer(0)
  myPen.speed(0)
  myPen.color("#000000")
  myPen.hideturtle()

  drawGrid(grid,[]) 
  myPen.getscreen().update()
  sleep(1)

  solved = solveGrid(grid)
  if solved:
    print("Sudoku Grid Solved")
    text("Sudoku Grid Solved",-110,-190,20)
    myPen.clear()
    drawGrid(grid,[]) 
    myPen.getscreen().update()           
    #sleep(50000)
    
  else:  
    print("Cannot Solve Sudoku Grid")
    text("Cannot Solve Sudoku Grid",-130,-190,20)

  myPen.getscreen().update()

if __name__ == "__main__":

    mainTask()
