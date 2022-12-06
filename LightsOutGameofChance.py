import random
import string
import math
import sys

def howtoplay():
    print("""How to Play:
First, the player will pick a grid to play on.
Each cell in the "Lights Out, Game of Chance!" grid has lights that are on and off.
The lights that are on will have "+", the lights that are off will have "-".
Selecting a light will reverse the switch, but the adjacent lights (up, down, left, right)
may or may not be reversed. This will be random.
The overall goal of this game is to turn off all the lights on the grid.
The fewest moves taken, the better.

To place your move on a cell, type the letter of the column the cell is in
and the letter of the row the cell is in.
You can also enter "exit" to exit the game, "retry" to reset the
grid and retry, and "new" for a new game.""")
    print("\n")


def validsize(x):
    #determine if valid size is given
    if not x.isdigit():
        return False
    elif int(x)>=2 and int(x)<= 10:
        return True
    else:
        return False

def gridsize():
    #input for size of grid, use validsize to confirm
    #2x2 is possible
    print("What size would you like the grid to be? Enter size as Width x Height.")
    print("""For example, to play 5x5, enter "5x5" or for a rectangular 3x5, enter "3x5".
The minimum is 2x2, and the maximum is 10x10.""")
    while True:
        size = input()
        #split the size into width and height
        size = size.split("x")

        if validsize(size[0]) and validsize(size[1]):
            return [int(size[0]), int(size[1])]
        else:
            print('Enter size as example: "3x3". Minimum is 2, maximum is 10.')

def area(grid):
    #take width and height of grid, so it can be used to draw and index
    area = [len(grid), len(grid[0])]
    return area

def cellidentity(identity):
    # store identity of cell to fill the cells in the grid
    if identity:
        #on
        return '+'
    else:
        #off
        return '-'

def gridrow(grid, row):
    # store grid spaces in list
    #assign width and height
    width, height = area(grid) # height isn't used in this function
    gridrow = []
    rowint = int(row)
    for i in range(width):
        #index the grid for identity of cell and print it out 4 times per line
        gridrow.append(cellidentity(grid[i][rowint]) * 4)
    #print(gridrow)
    return gridrow

def drawgrid(grid):
    #print nxn grid using gridrow and cellidentity
    #use ascii to classify each cell for user
    #ascii digits start from 0, letters start with A
    width, height = area(grid)

    print('     ' + '    '.join(string.ascii_uppercase[0:width])) #assign x value to cells from A to the letter of final width
    print('  +' + ('----+'*(width))) # top line of the grid
    for x in range(height):
        print('  |' + '|'.join(gridrow(grid, x)) + '|') #columns
        print(string.ascii_uppercase[x] + ' |' + '|'.join(gridrow(grid, x)) + '|') #assigns y value to cells and columns depending on the row
        print('  |' + '|'.join(gridrow(grid, x)) + '|') #columns
        print('  +' + ('----+' * (width))) #prints row dividers until the rightmost line




def newgrid(width, height):
    #list of randomized true false values of cell to convert into a grid
    #run two loops for list within a list, append each list within the first list height - 1 amount of times
    #print(height)
    grid = [] #list for true false values of cell
    
    for i in range(width):
        randomnum = random.randint(1, 100000)
        light = randomnum%2
        #print(light)
        if light == 1:
            #light is on
            grid.append([True])
        else:
            #light is off
            grid.append([False])

    l = len(grid)
    for _ in range(height-1):
        for x in range(l):
            randomnum = random.randint(1, 100000)
            light = randomnum%2
            if light == 1:
                grid[x].append(True)
            else:
                grid[x].append(False)
        #print(grid)
    return grid 

def gridcopy(grid):
    #copy original grid in case of retry
    width, height = area(grid)
    gridcopy = newgrid(width, height)
    #print(gridcopy)
    for x in range(width):
        for y in range(height):
            #copy entirity of newgrid
            gridcopy[x][y] = grid[x][y]
    #print(gridcopy)
    return gridcopy

def letterToIndex(letter):
    #assign letter to number using ascii
    num = string.ascii_uppercase.find(letter)
    return num

def validcell(grid, x, y):
    width, height = area(grid)
    if x >= 0 and x < width and y >= 0 and y < height:
        return True
    else:
        return False

def playermove(grid, x, y):
    #definitely flip selected block
    if validcell(grid, x, y):
        grid[x][y] = not grid[x][y]
    #random flip to every adjacent block
    #left
    if validcell(grid, x-1, y):
        grid[x-1][y] = not grid[x-1][y]
        numleft = random.randint(1, 100)
        for number in range(numleft):
            grid[x-1][y] = not grid[x-1][y]
    
    #right
    if validcell(grid, x+1, y):
        grid[x+1][y] = not grid[x+1][y]
        numright = random.randint(1, 100)
        for number in range(numright):
            grid[x+1][y] = not grid[x+1][y]

    #below
    if validcell(grid, x, y-1):
        numabove = random.randint(1, 100)
        grid[x][y-1] = not grid[x][y-1]
        for number in range(numabove):
            grid[x][y-1] = not grid[x][y-1]
    
    #above
    if validcell(grid, x, y+1):
        grid[x][y+1] = not grid[x][y+1]
        numbelow = random.randint(1, 100)
        grid[x][y+1] = not grid[x][y+1]
        for number in range(numbelow):
            grid[x][y+1] = not grid[x][y+1]
            

def moves(grid):
    width, height = area(grid)
    while True:
        #print('Enter (A-', string.ascii_uppercase[width-1],')(A-',string.ascii_uppercase[height-1],'), in the form of (example) "AC", or quit, retry, or new:')
        print('Enter (A-%s)(A-%s), in the form of (example) "AC" (column then row), or quit, retry, or new:' % (string.ascii_uppercase[width-1], string.ascii_uppercase[height-1]))
    
        move = input().upper()

        if move == 'QUIT' or move == 'RETRY' or move == 'NEW':
            return move
        elif len(move) == 2 and validcell(grid, letterToIndex(move[0]), letterToIndex(move[1])):
            return [letterToIndex(move[0]), letterToIndex(move[1])]
        # else:
        #     print('Enter (A-%s)(A-%s), in the form of (example) "AC" (column then row), or quit, retry, or new:' % (string.ascii_uppercase[width-1], string.ascii_uppercase[height-1]))


def win(grid):
    #scan grid values to see if user won
    width, height = area(grid)
    for x in range(width):
        for y in range(height):
            if grid[x][y] == True:
                return False
    return True

def newgame():
    print("Do you want to play a new game, retry the same game, or quit playing? Enter: new/retry/quit")
    while True:
        move = input().upper()
        if move == "NEW":
            return "NEW"
        elif move == "RETRY":
            return "RETRY"
        elif move == "QUIT":
            return "QUIT"
        else:
            print('Please type in "new", "retry", or "quit."')

#main code for game

def game():
    while True:
        width, height = gridsize()

        gamegrid = newgrid(width, height)

        originalgrid = gridcopy(gamegrid) # for when the player wants to retry
        movestaken = 0
        #loop for the game
        while True:
            drawgrid(gamegrid)

            print("Turns taken:", movestaken)
            movestaken += 1
            move = moves(gamegrid)
            #options for new, retry, quit
            if move == "NEW":
                break
            elif move == 'RETRY':
                movestaken = 0
                gamegrid = gridcopy(originalgrid)
            elif move == 'QUIT':
                print('Thanks for playing!')
                #stop code entirely
                sys.exit()
            else:
                playermove(gamegrid, move[0], move[1])
            #if a player wins
            if win(gamegrid):
                drawgrid(gamegrid)
                # Player has won the game
                #print('\n')
                print("Great job! You finished the game in", movestaken, "moves!")
                #print('\n')
                
                move = newgame()
                if move == "NEW":
                    break
                elif move == 'RETRY':
                    gamegrid = gridcopy(originalgrid)
                    movestaken = 0
                    continue
                else:
                    print('Thank you for playing!')
                    #stop code entirely
                    sys.exit()

#runs the game
print("Welcome to Lights Out, Game of Chance!")
print("Would you like to learn how to play? (Yes/No)")
while True:
    if input().lower() == "yes":
        howtoplay()
        game()
    else:
        game()
