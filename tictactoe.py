import os
os.system("cls")
#create a board
board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
activePlayer = "X"
winner = None
gameRunning = True
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " +board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " +board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " +board[8])  
    
#take player input
def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "_":
        board[inp-1] = activePlayer
    else:
        print("Oops, wrong choice!")
        
     
#check for a win or tie
def checkHorizontally(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        return True
    
def checkVertically(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "_":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "_":
        winner = board[2]
        return True
    
def checkDiagonally(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "_":
        winner = board[2]
        return True
    
def checkTie(board):
    global gameRunning
    if "_" not in board:
        printBoard()
        print("It's a tie!")
        gameRunning = False

def checkWin():
    global gameRunning
    if checkHorizontally(board) or checkVertically(board) or checkDiagonally(board) == True:
        print(f"The winner is \"{winner}\"")
        gameRunning = False

#switch player
def switchPlayer():
    global activePlayer
    if activePlayer == "X":
        activePlayer = "O"
    else: 
        activePlayer = "X"


while gameRunning:
    printBoard(board)
    playerInput(board)
    os.system("cls")
    checkWin()
    checkTie(board)
    switchPlayer()