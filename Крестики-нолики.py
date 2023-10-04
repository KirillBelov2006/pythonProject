field = [i for i in range(1, 10)]


def draw_board(field):
    print("-------------")
    for i in range(3):
        print("|", field[0 + i * 3], "|", field[1 + i * 3], "|", field[2 + i * 3], "|")
        print("-------------")


def take_input(player_token):
    valid = False
    while not valid:
        player_response = int(input(("Куда поставим " + player_token + "? ")))

        if player_response >= 1 and player_response <= 9:
            if str(field[player_response - 1]) not in "XO":
                field[player_response - 1] = player_token
                valid = True
            else:
                print("Эта клеточка уже занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")


def check_win(field):
    win_sequence = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_sequence:
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[each[0]]
    return False


def main(field):
    counter = 0
    win = False
    while not win:
        draw_board(field)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            temp = check_win(field)
            if temp:
                print(temp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break

    draw_board(field)


main(field)