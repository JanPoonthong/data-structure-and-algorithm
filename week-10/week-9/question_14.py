import numpy as np


def set_matrix(USER_INPUT_ROW):
    matrix = []
    for i in range(USER_INPUT_ROW):
        matrix.append([0])

        for j in range(USER_INPUT_ROW):
            matrix[i].append(0)

    return matrix


def add_edge(matrix, input_list):
    for i in range(len(input_list)):
        if i == 0:
            continue
        matrix[input_list[i][0]][input_list[i][1]] = 1

    return matrix


def find_row_column():
    row_column_input = input().split(" ")
    row = row_column_input[0]
    column = row_column_input[1].rstrip()
    return [int(row), int(column)]


def user_input(USER_INPUT_ROW):
    input_list = []
    input_list.append(USER_INPUT_ROW)
    for i in range(USER_INPUT_ROW[1]):
        input_list.append(list(map(int, input().split())))
    return input_list


def main():
    USER_INPUT_ROW = find_row_column()
    matrix = set_matrix(USER_INPUT_ROW[1])
    input_list = user_input(USER_INPUT_ROW)
    matrix = add_edge(matrix, input_list)
    matrix = np.array(matrix)
    print(matrix)


main()
