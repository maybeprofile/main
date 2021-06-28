# печать игрового поля
def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])


test_board = ['$', 'x', 'x', 'x', 'x', 'o', 'x', 'x', 'o', 'x']
display_board(test_board)


# пользователь выбирает Х или О
def player_input():
    marker = ''

    while marker != 'x' and marker != 'o':
        marker = input('Игрок 1 - выберите Х или О: ')

    player1 = marker

    if player1 == 'x':
        player2 = 'o'
    else:
        player2 = 'x'

    return (player1, player2)


player1_marker, player2_marker = player_input()
print('игрок 1 выбрал: ' + player1_marker)
print('игрок 2 выбрал: ' + player2_marker)


# принимает и выводит значения на доску
def place_marker(board, marker, position):
    board[position] = marker


print(place_marker(test_board, '$', 5))
print(display_board(test_board))

# проверка выигрыша
