adj = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def valid(row, column):
    global steps

    if 0 <= row < 10 and 0 <= column < 10:
        if steps[row][column] == 0:
            return True
    return False


maze = []
ends = []
for r in range(10):
    maze.append(input())

steps = [[0] * 10 for r in range(10)]
for r in range(10):
    for c in range(10):
        if maze[r][c] == '#':
            steps[r][c] = -1
        if maze[r][c] == 'X':
            ends.append((r, c))

Queue = [(ends[0], 0)]
visited = set()

while Queue:
    (r, c), dist = Queue.pop(0)
    if (r, c) == ends[1]:
        print("Reached in:", dist)
        break
    for dr, dc in adj:
        rr, cc = r + dr, c + dc

        if not valid(rr, cc):
            continue
        if (rr, cc) in visited:
            continue

        visited.add((rr, cc))
        Queue.append(((rr, cc), dist + 1))
else:
    print("Not Reached")
