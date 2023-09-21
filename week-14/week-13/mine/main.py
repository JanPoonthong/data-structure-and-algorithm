adj = [(0, -1), (0, 1), (-1, 0), (1, 0)]
data = []
list_count = []


def read_input():
    global data
    vertex, edge = map(int, input().split())

    for i in range(vertex):
        data.append(list(map(int, input().split())))

    return vertex, edge


def valid(row, column, edge, vertex, data):
    if 0 <= row < vertex and 0 <= column < edge:
        if data[row][column] == 1:
            return True
        return False


def find_one_in_data():
    global data
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 1:
                return (i, j)


def bfs(vertex, edge):
    global list_count, data

    count = 1
    queue = [find_one_in_data()]
    visited = set()

    while queue:
        (r, c) = queue.pop()
        data[r][c] = 0

        for dr, dc in adj:
            rr, cc = r + dr, c + dc

            if not valid(rr, cc, edge, vertex, data):
                continue
            if (rr, cc) in visited:
                continue

            if data[rr][cc] == 1:
                count += 1

            visited.add((rr, cc))
            queue.append((rr, cc))

    list_count.append(count)

    return list_count


def main():
    global list_count, data
    vertex, edge = read_input()
    while True:
        if any(1 in sublist for sublist in data):
            bfs(vertex, edge)
        else:
            break

    print(max(list_count))


main()
