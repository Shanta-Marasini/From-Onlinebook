print('Hello Shiva baba my world')

b={
    1 : '',
    2 : '',
    3 : '',
    4 : '',
    5 : '',
    6 : '',
    7 : '',
    8 : '',
    9 : ''
}

#function to print board
def pboard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('----------')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('----------')
    print(board[7] + '|' + board[8] + '|' + board[9])


def isWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

turn ='X'
for i in range(9):
    pboard(b)
    print('turn for' + turn +'.Move to which space?')
    move = int(input())
    if isWinner(b,turn):
        print(f'{turn} won congrats1')
        break
    b[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

pboard(b)





