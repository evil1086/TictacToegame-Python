print("***************** TIC TAC TOE GAME ++++++++++++")

#player name declaration
player1 = input("please enter 1st player name")
player2 = input("please enter 2nd player name")

#sign distribution
print("Please choose sign'X' or 'O'")
player1_sign = input("")
print('{} select his/her sign'.format(player1),player1_sign)
player2_sign = input("")

#tic tac board display
print('{} select his/her sign'.format(player2),player2_sign)
test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
display_board(test_board)

#Marker point at
count = 0
for count in range(9):
    if count % 2 == 0:
        mov_count = input("{}:place your marker in single position".format(player1))
        print("Marker points to location",mov_count)
        display_board(test_board)

        def win_check(mov_count):
            if mov_count == [7,5,2] or [1,5,9] or [7,4,1] or [8,5,2] or [9,6,3] or [1,2,3] or [4,5,6] or [7,8,9]:
                print("{}.win this game".format(player1))
            else:
                print("hard luck ,want to play again")
            win_check(mov_count)
    else:
        mov_count = input("{}:place your marker in single position".format(player2))
        print("Marker points to location",mov_count)

        def win_check(mov_count):
            if mov_count == [7,5,2] or [1,5,9] or [7,4,1] or [8,5,2] or [9,6,3] or [1,2,3] or [4,5,6] or [7,8,9]:
                print("{}.win this game".format(player2))
            else:
                print("hard luck ,want to play again")
            win_check(mov_count)







