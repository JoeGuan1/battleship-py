import array as arr

min_length = 0
max_length = 5

def player_input():
    ships = []

    print ("Please enter in your ship coordinates. Select numbers between 0-10.")

    total = 0
    ship_num = 6

    while total < ship_num:
        col = int (input("Select a column\n"))
        if col < min_length or col > max_length:
            print ("Invalid column. Please enter a number between 0-10")
            continue
        row = int (input("Select a row\n"))
        if row < min_length or row > max_length:
            print ("Invalid row. Please enter a number between 0-10")
            continue
        points = [col,row]
        if points in ships:
            print("Ship coordinates already entered. Please enter a new coordinates.")
            continue
        ships.append(points)
        total +=1

    #print (ships)

    return ships

def create_board ():
    test_board = []

    for i in range (max_length):
        temp_board = []
        for j in range (max_length):
            temp_board.append("O")
        test_board.append(temp_board)
    
    return test_board

def print_board (board):
    for n in board:
        print (n)

def check_board (board, check):
    if check in board:
        return True
    else:
        return False

player_1 = player_input()
player_2 = player_input()

#print (player_1)
#print (player_2)

board1 = create_board()
board2 = create_board()

#print (board1)
#print (board2)


hits1 = 0
hits2 = 0
one = True
guessed1 = []
guessed2 = []
while hits1 < 6 and hits2 < 6:
    if one:
        print("Player 1's Turn")
        print_board(board2)
        col = int (input("Select a column\n"))
        row = int (input("Select a row\n"))
        find = [col,row]
        print (find)
        if check_board (guessed2, find):
            print("You've already guessed that point. Please enter a different point.")
            continue
        elif find in player_2:
            guessed2.append(find)
            hits1 +=1
            board2[col][row] = "X"
            player_2.pop(player_2.index(find))
            print ("HIT")
            one = False
        else:
            board2[col][row] = "~"
            guessed2.append(find)
            print ("MISS")
            one = False
    else:
        print("Player 2's Turn")
        print_board(board1)
        col = int (input("Select a column\n"))
        row = int (input("Select a row\n"))
        find = [col,row]
        print (find)
        if check_board (guessed1, find):
            print("You've already guessed that point. Please enter a different point.")
            continue
        elif find in player_1:
            guessed1.append(find)
            hits2 +=1
            board1[col][row] = "X"
            player_1.pop(player_1.index(find))
            print ("HIT")
            one = True
        else:
            guessed1.append(find)
            board1[col][row] = "~"
            print ("MISS")
            one = True

if one:
    print ("PLAYER 1 WINS!")

else: 
    print ("PLAYER 2 WINS!")
