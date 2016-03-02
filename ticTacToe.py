def printBoard(board):
    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    
theboard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
theboard
{'top-L': ' ', 'low-L': ' ', 'top-R': ' ', 'low-M': ' ', 'top-M': ' ', 'mid-M': ' ', 'mid-L': ' ', 'low-R': ' ', 'mid-R': ' '}
import pprint
pprint.pprint(theboard)
{'low-L': ' ',
 'low-M': ' ',
 'low-R': ' ',
 'mid-L': ' ',
 'mid-M': ' ',
 'mid-R': ' ',
 'top-L': ' ',
 'top-M': ' ',
 'top-R': ' '}
def printboard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
	
printboard(theboard)
 #tic tac toe board is printed
 
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################
theboard = {'top-L': 'x', 'top-M': 'x', 'top-R': 'x', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
theboard
import pprint
pprint.pprint(theboard)
def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')
    
    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board          #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################
    
    if board['top-L'] == board['top-M'] == board['top-R'] == player:
	return true
    
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer #assigns "turn" to each starting player's turn
    for i in range(9): #we use for loop for a block of code up to 9 times
        printBoard(board) #tic tac toe blank board will be printed
        print('Turn for ' + turn + '. Move on which space?') #gets active player's move and prints Turn for X. (Or prints Turn for O). Move on which space? o
        move = input() #user input will update the board.
        board[move] = turn #swaps active player
        if( checkWinner(board, 'X') ): #checks the board if X won
            print('X wins!') #if X wins, prints: X wins!
            break #terminates current loop checking for X winner
        elif ( checkWinner(board, 'O') ): #checks the board if O won
            print('O wins!') #if O wins, prints: O wins!
            break #terminates current loop checking for O winner
    
        if turn == 'X': #if it's X's turn, 
            turn = 'O' #change turn to O
        else: #or else, 
            turn = 'X' #change turn to X
        
    printBoard(board)
    
