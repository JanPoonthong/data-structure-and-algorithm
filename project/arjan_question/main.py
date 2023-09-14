adj = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def read_input(n_read_lines):
    maze = []
    for i in range(n_read_lines):
        maze.append(list(map(int, input().split())))

    # X = -1
    # maze[0][0] = X
    # maze[len(maze) - 1][len(maze) - 1] = X
    return maze


def valid(row, column, n_read_lines, maze):
    if 0 <= row < n_read_lines and 0 <= column < n_read_lines:
        if maze[row][column] == 0:
            return True
        return False


def main():
    n_read_lines = int(input())
    maze = read_input(n_read_lines)

    queue = [((0, 0), 0)]
    visited = set()

    while queue:
        (r, c), dist = queue.pop()
        if (r, c) == (len(maze) - 1, len(maze) - 1):
            print("yes")
            break
        for dr, dc in adj:
            rr, cc = r + dr, c + dc

            if not valid(rr, cc, n_read_lines, maze):
                continue
            if (rr, cc) in visited:
                continue

            visited.add((rr, cc))
            queue.append(((rr, cc), dist + 1))
    else:
        print("no")


main()
