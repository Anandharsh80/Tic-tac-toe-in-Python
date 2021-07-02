#creating the board for game
board=[['_', '_', '_'],['_', '_', '_'],['_', '_', '_']]


#function to display the board
def display():
    print('')
    print('Current Board')
    for el in board:
        line = '  '.join(el)
        print(line)
    print('')
        
#function to check for winner 
def win(a):
    if (board[0][0]==a) and (board[1][1]==a) and (board[2][2]==a):
        return a
    if (board[0][2]==a) and (board[1][1]==a) and (board[2][0]==a):
        return a
    for i in range(0,3):
        if (board[i][0]==a) and (board[i][1]==a) and (board[i][2]==a):
            return a
        if (board[0][i]==a) and (board[1][i]==a) and (board[2][i]==a):
            return a
        
#function to display the rules      
def print_rules(): 
    print('TIC-TAC-TOE GAME')
    print('(by Harsh Anand)')
    print('\nRULES:-')
    print("1. Player that goes first will use 'X' and Player that goes second will use 'O'")
    print('2. Rows are numbered [0,1,2] from top to bottom and Colums are numbered [0,1,2] from left to right')
    print('3. In each turn enter a valid row and column that is not already filled')
    
    
    
    
#driver code
print_rules()
display()
for i in range(0,9):
    if i%2==0:
        user = 'X'
    else:
        user = 'O'
    row = -1
    column = -1
    winner = ''
    
    #inseting X or O at user entered location
    while True:
        
        #taking input for row value
        while True:
            row = int(input('Enter the row : '))
            if (row >= 0) and (row <= 2):
                break
            print('\nINVALID CHOICE\n')
            
            
        #taking input for column value 
        while True:
            column = int(input('Enter the column : '))
            if (column >= 0) and (column <= 2):
                break
            print('\nINVALID CHOICE\n')
    
        
        #checking if the place is already marked 
        if board[row][column] == '_':
            board[row][column] = user
            break
        else:
            print('\nPLACE IS ALREADY MARKED\n')
            
            
    #display current scenario of board   
    display()
    
    #checking if current player has won 
    winner = win(user)
    if (winner==user):
        print('{} wins'.format(user))
        break
    
    
    #if no player wins even at last try, then game draws
    if (i==8):
        print('Game Draw')
