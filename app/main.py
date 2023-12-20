from random import randrange

def display_board(board):
    print('+-------'*3, '+', sep="")
    for row in range(3):
        print('|       '*3, '|', sep="")
        for col in range(3):
            print('|   '+str(board[row][col]) + "   ", end="")
        print('|')
        print('|       '*3,'|',sep="")
        print('|-------'*3,'+',sep="")
# function that’s gives the permission to do a move
def enter_move(board):
    ok= False
    while not ok:
        move = input("enter your move ")
        ok = len(move)==1 and move>='1' and move<='9'
        if not ok:
            print("bad move  - repeat your input")
            continue
        move = int(move)-1
        row=move//3
        col=move%3
        signe= board[row][col]
        ok = signe not in ['O','X']
        if not ok:
            print('field already occupied - repeat your input')
            continue
    board[row][col]= 'O'
def make_list_of_free(board):
    free=[]
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X','O']:
                free.append((row,col))
    return free
def victory_for(board,sgn):
    if sgn == "X":
        who= 'me'
    elif sgn == "O":
        who='you'
    else:
        who = None
    cross1=cross2=True
    for rc in range(3):
        if board[rc][0]== sgn and board[rc][1] == sgn and board[rc][2] == sgn:
            return who
        if board[0][rc]== sgn and board[1][rc] == sgn and board[2][rc] == sgn:
            return who
        if board[rc][rc] != sgn:  #check the first diagonal
            cross1=False
        if board[2-rc][rc] != sgn:    #check the second diangonal
            cross2=False
        if cross1 or cross2:
            return who
def draw_move(board):
    free = make_list_of_free(board)
    cnt = len(free)
    if cnt >0:
        this = randrange(cnt)
        row, col = free[this]
        board[row][col]='X'
board = [[3*j+i+1 for i in range(3)]for j in range(3)]
board[1][1] = 'X'
free = make_list_of_free(board)
human_turn = True
while len(free):
    display_board(board)
    if human_turn:
        enter_move(board)
        victor= victory_for(board,'O')
    else:
        draw_move(board)
        victor = victory_for(board,'X')
    if victor != None:
        break
    human_turn = not human_turn
    free = make_list_of_free(board)

display_board(board)
if victor == 'you':
    print("YOU WON 🎊")
elif victor == 'me':
    print('I  WON 🎊')
else:
    print("Tie!")
