import time,os
#######################################################################################################

# two players choose their symbol X or O
class Player():

    def __init__(self,name,symbol):
        self.name = name
        self.symbol = symbol
    
    def __str__(self):
        return f"Player Name: {self.name}   Player Symbol: {self.symbol}"
 
    # player A choose its Symbol
    # if Player A chose O then Player B is X otherwise Player B is O

#######################################################################################################

def boardprint():
  
    print("\t\t\t\t** TIC TAC TOE **\n")

    print(f"\t\t{player1}")
    print(f"\t\t{player2}\n")
    
    for row in board:
        print("          ".join(row))
    print("\n")

#######################################################################################################

def update_board():
    os.system('cls')
    boardprint()

#######################################################################################################

# create a Matrix of 3 rows and 3 columns for tictactoe
board = [['Q','W','E'],['A','S','D'],['Z','X','C']]
my_dict = {
    'q':(0,0),'w':(0,1),'e':(0,2),
    'a':(1,0),'s':(1,1),'d':(1,2),
    'z':(2,0),'x':(2,1),'c':(2,2),   

}

print("\t\t\t\t*******    WELCOME TO TIC TAC TOE    *******\n")
print("\t\t\t\t*******     WE HAVE TWO PLAYERS     *******\n")

symbol1 = ''
symbol2 = ''
entry = ''

#######################################################################################################

# COLLECTING USER DETAILS
name1 = input("Player1 - Please Enter Your Name: ")

while symbol1 not in ('X', 'O'): 
    symbol1 = input(f"Hi {name1}! Please Choose Your Symbol (X or O): ")   

if symbol1 == 'X':
    symbol2 = 'O'
else:
    symbol2 = 'X'

name2 = input("\nPlayer2 - Please Enter Your Name: ")
print(f"Hi {name2}! {name1} has choosen {symbol1} so your Symbol is {symbol2}\n")

#######################################################################################################

print("\t\t\t\tSTRETCH YOUR FINGERS! LETS BEGIN\n")

# INTIALISING PLAYERS
player1 = Player(name1,symbol1)
player2 = Player(name2,symbol2)

time.sleep(5)

# Game started
update_board()

game_on = True

while game_on is True:

    while entry not in my_dict:
        entry = input(f"{name1}! Please choose mark your position: ")
    x,y = my_dict[entry]
    board[x][y] = player1.symbol
    update_board()
    entry = ''

    while entry not in my_dict:
        entry = input(f"{name2}! Please choose mark your position: ")
    x,y = my_dict[entry]
    board[x][y] = player2.symbol
    update_board()
    entry = ''


    r1 = board[my_dict['w']] == board[my_dict['q']] and  board[my_dict['e']] == board[my_dict['q']]
    r2 = board[my_dict['s']] == board[my_dict['a']] and  board[my_dict['d']] == board[my_dict['a']]
    r3 = board[my_dict['x']] == board[my_dict['z']] and  board[my_dict['c']] == board[my_dict['z']]

    c1 = board[my_dict['a']] == board[my_dict['q']] and  board[my_dict['z']] == board[my_dict['q']]
    c2 = board[my_dict['s']] == board[my_dict['w']] and  board[my_dict['x']] == board[my_dict['w']]
    c3 = board[my_dict['d']] == board[my_dict['e']] and  board[my_dict['c']] == board[my_dict['e']]

    d1 = board[my_dict['e']] == board[my_dict['s']] and  board[my_dict['z']] == board[my_dict['s']]
    d2 = board[my_dict['q']] == board[my_dict['s']] and  board[my_dict['c']] == board[my_dict['s']]


    if (r1 or r2 or r3 or c1 or c2 or c3 or d1 or d2 ):
        game_on = False
        break

print("\t\t\t\t******** GAME OVER ****************\n")
input("Press Enter to Exit!")