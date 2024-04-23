#Tirath Singh
#built in Ottawa in 2024

def main():

    #Declare a global value
    global board
    global currentStack

    #Initial Welcome message.
    print("Game Rules:")
    print("OpponentA = X and OpponentB = O")
    print("Good Luck")


    board = [
                '1','2','3',
                '4','5','6',
                '7','8','9'
            ]

    currentStack = []
    GameOver = False
    move = 0
    opponent_B = 0

    currentMove = 'X'

    printBoard()

    while GameOver==False:
        #Get the input from user. First move will always be X
        move = int(input(f"Opponent {currentMove} Turn\n"))

        #Check weather a move alredy exists and also check if the board is full.
        if MoveExist(move) == False:
            setBoard(move,currentMove)
            currentStack.append(move)
            printBoard()
                
            #Check if the current board is completely filled
            if len(currentStack)>9:
                GameOverWithoutWin()
                GameOver=True

            #Check the board for the winner
            elif checkBoard():
                GameOverMessage(currentMove)
                GameOver=True

            #Switch the move turn
            if currentMove == 'X':
                currentMove = 'O'
            elif currentMove == 'O':
                currentMove = 'X'

        else:
            printError()


#Funtions.


# This function set the value in the array for a given move.
def setBoard(opponent,value):
    board[opponent-1] = value


# This function prints the board on the console.
def printBoard():
    print("Current board")
    nextLine = 0
    for i in board:
        if nextLine==3:
            nextLine=0
            print()
        print(i,end = " ")
        nextLine = nextLine + 1
    print()

# This function check if the board full or move already made.
def MoveExist(opponent):
    for i in currentStack:
        if i==opponent or i > 9:
            return True
    return False

#This function check print the error message
def printError():
    print("Value out of range or already exist")

#Check the board and if there is a winner. Board is a global value.
def checkBoard():
    #A Winner board
    if board[0] == board[1] == board[2]:
        return True
    elif board[3] == board[4] == board[5]:
        return True
    elif board[6] == board[7] == board[8]:
        return True
    elif board[0] == board[3] == board[6]:
        return True
    elif board[1] == board[4] == board[7]:
        return True
    elif board[2] == board[5] == board[8]:
        return True
    elif board[0] == board[4] == board[8]:
        return True
    elif board[2] == board[4] == board[6]:
        return True
    else:
        return False


#This function check print the game over message
def GameOverMessage(OpponentChar):
    print("---------------------")
    print("Game Over")
    print(f"Opponent {OpponentChar} Won")
    print("---------------------")

#This function check print the game over message if no winner
def GameOverWithoutWin():
    print("---------------------")
    print("Game Over Without winner")
    print("---------------------")


#Main Funtion
if __name__ == '__main__':
    main()