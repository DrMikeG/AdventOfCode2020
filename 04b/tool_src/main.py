#Backtracking Algorithm - Sudoku Solver - www.101computing.net/backtracking-algorithm-sudoku-solver/
import turtle
from random import randint
from time import sleep

myPen = turtle.Turtle()
topLeft_x=-150
topLeft_y=150

greyCells = [(1,3),(2,8),(3,1),(5,5),(5,6),(6,1),(6,2),(6,7),(8,0),(8,1),(8,3)]

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
            if isGridCellOnWalkAlready(walk,(row,col)):
                myPen.pencolor("red")
            else :
                myPen.pencolor("black")
        if grid[row][col]!=0:
          text(grid[row][col],topLeft_x+col*intDim+9,topLeft_y-row*intDim-intDim+8,18)


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
    for p in greyCells:
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


def countSnakeCellsIn8OfCell(gridCell,walk):
  (r,c) = gridCell
  count = 0
  for r1 in [-1,0,1]:
    for c1 in [-1,0,1]:
        absSum = abs(r1) + abs(c1)
        if (absSum > 0):
          neighbour = (r+r1,c+c1)
          if (isGridCellOnWalkAlready(walk,neighbour)):
            count = count + 1
  return count


def countSnakeCellsNESWOfCell(gridCell,walk):
  (r,c) = gridCell
  count = 0
  for r1 in [-1,0,1]:
    for c1 in [-1,0,1]:
      # don't allow the diagonals or middle
      absSum = abs(r1) + abs(c1)
      if (absSum < 2 and absSum > 0):
        neighbour = (r+r1,c+c1)
        if (isGridCellOnWalkAlready(walk,neighbour)):
          count = count + 1
  return count

def printSnake(grid,walk):
  for r in range(0,9):
    row = []
    for c in range(0,9):
      if isGridCellOnWalkAlready(walk,(r,c)):
        row.append(str(grid[r][c]))
      else:
        row.append("_")
    print(list(row))
  print("")

def checkSnakeCountAroundGreyCell(grid,walk,greyCellRC):
  neededCount = grid[greyCellRC[0]][greyCellRC[1]]
  snakeCount = countSnakeCellsIn8OfCell(greyCellRC,walk)
  return neededCount == snakeCount

def checkSnake(grid,walk):
  # Each snake cell can neighbour at most 2 other snake cells
  
  #printSnake(grid,walk)
  #print(walk)
  for p in walk:
      if countSnakeCellsNESWOfCell(p[0],walk) > 2 :
        return False
      if countSnakeCellsNESWOfCell(p[1],walk) > 2 :
        return False

  #Around a grey cell, there can only be n snake cells
  for greyCellRC in greyCells :
    if not checkSnakeCountAroundGreyCell(grid,walk,greyCellRC):
      return False

  return True

def solvePalendromeWalk(grid,walk):
    
    #myPen.clear()
    #drawGrid(grid,walk) 
    #myPen.getscreen().update()

    # the current end tuple is two values on the grid
    (snakeA,snakeB) = walk[-1]

    if (walk == [((4, 0), (7, 1)), ((4, 1), (7, 2)), ((5, 1), (7, 3)), ((5, 2), (7, 4)), ((5, 3), (8, 4)), ((5, 4), (8, 5)), ((4, 4), (8, 6)), ((3, 4), (7, 6)), ((3, 3), (7, 7)), ((2, 3), (7, 8)), ((2, 2), (6, 8)), ((1, 2), (5, 8)), ((0, 2), (4, 8)), ((0, 3), (4, 7)), ((0, 4), (3, 7)), ((0, 5), (3, 6)), ((1, 5), (2, 6)), ((1, 6), (1, 6))]):
      print("This should be the solution")

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
                    else:
                      return True #solved!

    return False

#A function to check if the grid is full
def checkGrid(grid):
  for row in range(0,9):
      for col in range(0,9):
        if grid[row][col]==0:
          return False


  if (True):
    # must start and end of the same
    if (grid[4][0] != grid[7][1]):
        return False

    print("Suduku solution - looking for snake")

    # Testing walk 
    
    
    #myPen.clear()
    #drawGrid(grid,walk) 
    #myPen.getscreen().update()
    
    walk = []
    walk.append(((4,0),(7,1)))

    if (solvePalendromeWalk(grid,walk)):
      myPen.clear()
      drawGrid(grid,walk) 
      myPen.getscreen().update()
      return True

    return False

  return True 




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

  # pre-solve sudoku to test snake
  
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
    #myPen.clear()
    #drawGrid(grid,[]) 
    #myPen.getscreen().update()           
    #sleep(50000)
    
  else:  
    print("Cannot Solve Sudoku Grid")
    text("Cannot Solve Sudoku Grid",-130,-190,20)

  myPen.getscreen().update()
  input("Press Enter to continue...")
    
if __name__ == "__main__":

    mainTask()    
