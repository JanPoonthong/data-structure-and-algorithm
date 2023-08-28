def DFS_visit(s, adj, visited, stack):
    for v in adj[s]:
        if not visited[v]:
            visited[v] = True
            DFS_visit(v, adj, visited, stack)
    stack.append(s)


def topological_sort(V, adj):
    visited = [False] * V
    stack = []

    for s in range(V):
        if not visited[s]:
            visited[s] = True
            DFS_visit(s, adj, visited, stack)
    stack.reverse()
    return stack


def find_row_column():
    row_column_input = input().split()
    row = int(row_column_input[0])
    column = int(row_column_input[1])
    return row, column


def check_number(user_input_row):
    data = []
    for _ in range(user_input_row[1]):
        row_and_column = input().split()
        data.append((int(row_and_column[0]), int(row_and_column[1])))
    return data


def user_input(length, data):
    input_list = {vertex: [] for vertex in range(length)}
    for i in data:
        input_list[i[0]].append(i[1])
    return input_list


def main():
    user_input_row = find_row_column()
    data = check_number(user_input_row)
    input_list = user_input(user_input_row[0], data)
    stack_result = topological_sort(user_input_row[0], input_list)
    for i in stack_result:
        print(i)


main()
