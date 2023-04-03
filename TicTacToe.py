board = ["-", "-" ,"-" ,
        "-" ,"-" ,"-" ,
        "-" , "-", "-"]

# if game is still going
gameStillGoing = True

# Winner
winner = None

# Whos turn is it
currentPlayer = 'X'



# display board
def displayBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])




def playGame():
    
    #display initial board
    displayBoard()

    # loop while the game is still going
    while gameStillGoing:
        
        # handle a single turn 
        handleTurn(currentPlayer)
        
        # check if the game has ended
        checkIfGameOver()

        # Flip to the other player
        flipPlayer()

    # Game has ended
    if winner == 'X' or winner == 'O':
        print(winner + ' won.')
    elif winner == None:
        print('Tie.')




def checkIfGameOver():
    checkIfWin()
    checkIfTie()




def checkIfWin():
    # Set up global variables
    global winner
    
    # check rows
    rowWinner = checkRows()
    
    # check columns
    columnsWinner = checkColumns()
    
    # check diagonals
    diagonalsWinner = checkDiagonals()

    if rowWinner:
        winner = rowWinner
    
    elif columnsWinner:
        winner = columnsWinner
    
    elif diagonalsWinner:
        winner = diagonalsWinner
    
    else:
        winner = None
    
    return



def checkRows():
    # set up global variables
    global gameStillGoing

    # check if any of the rows have all the same value
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    # if any row does have a match, end game
    if row_1 or row_2 or row_3:
        gameStillGoing = False
        # Return the winner
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]    
    return

def checkColumns():
    # set up global variables
    global gameStillGoing

    # check if any of the columns have all the same value
    columns_1 = board[0] == board[3] == board[6] != '-'
    columns_2 = board[1] == board[4] == board[7] != '-'
    columns_3 = board[2] == board[5] == board[8] != '-'

    # if any row does have a match, end game
    if columns_1 or columns_2 or columns_3:
        gameStillGoing = False
        # Return the winner
    if columns_1:
        return board[0]
    if columns_2:
        return board[1]
    if columns_3:
        return board[2]    
    return

def checkDiagonals():
    # set up global variables
    global gameStillGoing

    # check if any of the diagonals  have all the same value
    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[6] == board[4] == board[2] != '-'

    # if any row does have a match, end game
    if diagonal_1 or diagonal_2 :
        gameStillGoing = False
        # Return the winner
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[6]    
    return



def checkIfTie():
    
    global gameStillGoing
    
    if '-' not in board:
        gameStillGoing = False

    return




def flipPlayer():

    global currentPlayer

    if currentPlayer == 'X':
        currentPlayer = 'O'
    elif currentPlayer == 'O':
        currentPlayer = 'X'
    return


# handle a trun of a player
def handleTurn(player):
    # aleg locul unde o sa fie asezat x
    print(player +'`s turn.')
    position = input('Choose a position from 1-9: ')
    position = int(position) - 1

    # valid = False
    #while not valid:


       # while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        #    position = input('Invalid input. Choose a position from 1-9: ')
        
      #  if board[position] == "-":
       #     valid = True
        #else:
         #   print('You cant go there. Go again.')


    # setezi unde este asezat x
    board[position] = player
    displayBoard()

playGame()


 