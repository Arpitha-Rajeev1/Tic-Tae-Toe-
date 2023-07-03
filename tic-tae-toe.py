def add(x,y,z):
    return x+y+z

def printBoard(xState, zState):
    zero = 'X' if xState[0] else ('Z' if zState[0] else 0)
    one = 'X' if xState[1] else ('Z' if zState[1] else 0)
    two = 'X' if xState[2] else ('Z' if zState[2] else 0)
    three = 'X' if xState[3] else ('Z' if zState[3] else 0)
    four = 'X' if xState[4] else ('Z' if zState[4] else 0)
    five = 'X' if xState[5] else ('Z' if zState[5] else 0)
    six = 'X' if xState[6] else ('Z' if zState[6] else 0)
    seven = 'X' if xState[7] else ('Z' if zState[7] else 0)
    eight = 'X' if xState[8] else ('Z' if zState[8] else 0)
    
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")

def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1,4,7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:        
        if(add(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X wins")
            return 1
        if(add(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("Z wins")
            return 0
    return -1

def val(xState, zState):
    while True:
        value = int(input("Please enter a value: "))
        if(not(xState[value]) and not(zState[value])):
            break
    return value

xState = [0,0,0,0,0,0,0,0,0]
zState = [0,0,0,0,0,0,0,0,0]
turn = 1 # 1 for X and 0 for O
print('Welcome to Tic Tat Toe')

while True:
    if(turn == 1):
        print("X's Chance")
        value = val(xState, zState)
        xState[value] = 1
    else:
        print("Z's Chance")
        value = val(xState, zState)
        zState[value] = 1
        
    printBoard(xState, zState)
    
    if(checkWin(xState, zState) != -1):
        print("Match over")
        break
    turn = not(turn)
