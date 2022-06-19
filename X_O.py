def greeting():
    print("  Приветствуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики! ")
    print("-------------------")
    print("  Игра рассчитана  ")
    print(" на двоих игроков. ")
    print("   Формат ввода:   ")
    print("     x y , где     ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")


greeting()

board = [[" ", " ", " "] for i in range(3)]


def u_turn():
    while True:
        coords = input("         Ваш ход: ").split()

        if len(coords) != 2:
            print(" Введите 2 значения координат через пробел для постановки своего знака ")
            continue
        x, y = coords
        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите численные значения от 0 до 2 ")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне игрового поля ")
            continue
        if board[x][y] != " ":
            print(" Клетка занята, попробуйте другую ")
            continue
        return x, y


u_turn()


def grid():
    print()
    print(f"   | 0 | 1 | 2 |")
    print(" --------------- ")
    for i, row in enumerate(board):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print(" --------------- ")
    print()


grid()


def win_cond():
    win_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                 ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                 ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for coord in win_coord:
        symbols = []
        for c in coord:
            symbols.append(board[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print(" Выиграл игрок с X")
            return True
        if symbols == ["O", "O", "O"]:
            print(" Выиграл игрок с O")
            return True
    return False


def main():
    counter = 0
    while True:
        counter += 1
        grid()
        if counter % 2 == 1:
            print(" Ход игрокa с X")
        else:
            print(" Ход игрока с O")
        x, y = u_turn()
        if counter % 2 == 1:
            board[x][y] = "X"
        else:
            board[x][y] = "O"
        if win_cond():
            break
        if counter == 9:
            print("Ничья!")
            break


main()
