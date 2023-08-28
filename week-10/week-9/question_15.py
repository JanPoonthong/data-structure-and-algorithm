""""
9 8
0 1
1 2
3 2
3 4
4 5
2 5
0 7
6 7

0 = [1, 7]
"""


def make_collection_adjacency_list_directed(input_list):
    temp = input_list[1:]
    print(temp)
    share_pairs = {}
    for i in range(len(temp)):
        if temp[i][0] in share_pairs:
            if temp[i][1] in share_pairs[temp[i][0]]:
                continue
            share_pairs[temp[i][0]].append(temp[i][1])
        else:
            share_pairs[temp[i][0]] = [temp[i][1]]
        for j in range(i + 1, len(temp)):
            if temp[i][0] == temp[j][0]:
                if temp[i][0] in share_pairs:
                    share_pairs[temp[i][0]].append(temp[j][1])
                else:
                    share_pairs[temp[i][0]] = [temp[j][1]]
    print(share_pairs)


def make_collection_adjacency_list_undirect(input_list):
    temp = input_list[1:]
    print(temp)
    share_pairs = {}
    for num in range(len(temp)):
        for i in range(len(temp)):
            if num in temp[i]:
                if num != temp[i][0]:
                    if num in share_pairs:
                        share_pairs[num].append(temp[i][0])
                    else:
                        share_pairs[num] = [temp[i][0]]
                else:
                    if num in share_pairs:
                        share_pairs[num].append(temp[i][1])
                    else:
                        share_pairs[num] = [temp[i][1]]
    print(share_pairs)


def find_row_column():
    row_column_input = input().split(" ")
    row = row_column_input[0]
    column = row_column_input[1].rstrip()
    return [int(row), int(column)]


def user_input(user_input_row):
    input_list = [user_input_row]
    for i in range(user_input_row[1]):
        input_list.append(list(map(int, input().split())))
    return input_list


def main():
    user_input_row = find_row_column()
    input_list = user_input(user_input_row)
    # make_collection_adjacency_list_undirect(input_list)
    make_collection_adjacency_list_directed(input_list)


main()
