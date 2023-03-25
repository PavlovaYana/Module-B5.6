print ("Добро пожаловать в игру крестики-нолики!")
# заведем поле, где будем играть
board = list(range(1,10))
# введем функцию, которая определяет игровое поле 3 на 3 с числами от 1 до 9
def game_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-" * 13)

# введем функцию, отвечающую за пользовательский ввод
def user_input(player_game):
    valid = False
    while not valid:
        player_answer = input("Куда поставить " + player_game + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Введите число.")
            continue
        if player_answer >=1 and player_answer <= 9:
            if str(board[player_answer-1]) not in "XO":
                board[player_answer-1] = player_game
                valid = True
            else:
                print("Это клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9!")

# введем функцию, проверяющую победу
def check_win (board):
    win_position = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6)
)
    for every in win_position:
        if board[every[0]] == board[every[1]] == board[every[2]]:
            return board[every[0]]
    return False

# вводим функцию, которая будет работать, пока один из игроков не выиграет
def main_board(board):
    #заведем счетчик
    counter = 0
    win = False
    while not win:
        game_board(board)
        if counter % 2 == 0:
            user_input("X")
        else:
            user_input("O")
        counter += 1
        if counter > 4:
            check = check_win(board)
            if check:
                print("Победа!!!")
                win = True
                break
        if counter == 9:
            print("Ничья")
            break
    game_board(board)
main_board(board)

input("Нажмите Enter для выхода.")