# игровое поле
board = [['-' for i in range(3)] for i in range(3)]

# отображение игрового поля
def map():
    print(' 0 1 2')
    for a, b in enumerate(board):
        print(f'{a} {" ".join(b)}')
# map()
# проверка победы
def check_win(player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# ходы
now_player = 'x'
while True:
    map()
    print(f"Ход игрока {now_player}")

    while True:
        q = int(input("Введите номер строки (0, 1, 2): "))
        w = int(input("Введите номер столбца (0, 1, 2): "))
        if 0 <= q < 3 and 0 <= w < 3 and board[q][w] == '-':
            break
        else:
            print("Некорректные координаты, попробуйте снова.")
    board[q][w] = now_player
    if check_win(now_player):
        map()
        print(f"Игрок {now_player} победил!")
        break
    elif all(board[i][j] != '-' for i in range(3) for j in range(3)):
        map()
        print("Ничья!")
        break
    now_player = 'o' if now_player == 'x' else 'x'




