"""
    - Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""

from random import randint

BOARD_SIZE = 8


def is_queen_beat(positions: list[list[int]]) -> bool:
    chessboard_x = []
    chessboard_y = []

    for position in range(BOARD_SIZE):
        x, y = positions[position]
        chessboard_x.append(x)
        chessboard_y.append(y)

    for i in range(BOARD_SIZE):

        for j in range(i + 1, BOARD_SIZE):

            if chessboard_x[i] == chessboard_x[j] or chessboard_y[i] == chessboard_y[j] \
                    or abs(chessboard_x[i] - chessboard_x[j]) == abs(chessboard_y[i] - chessboard_y[j]):
                return True

    return False


# task4
def successful_position(count_of_positions) -> list:
    position = []
    count = 1
    count_iter = 0
    while count <= count_of_positions:
        count_iter += 1
        i = 0
        while i < BOARD_SIZE:
            x = randint(1, 8)
            y = randint(1, 8)
            if [x, y] not in position:
                position.append([x, y])
                i += 1

        if is_queen_beat(position):
            print(position, 'iter = ', count_iter)
            count += 1
        position.clear()
