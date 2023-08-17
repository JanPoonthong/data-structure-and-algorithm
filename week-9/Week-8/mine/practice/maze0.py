# relative distance of above, below, left, and right cells
adj = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def valid(row, column):
    # return True if coordinate (r,c) is not outside the matrix
    # and is not a part of a wall

    global steps

    if row >= 0 and row < 10 and column >= 0 and column < 10:
        if steps[row][column] == 0:
            return True
    return False


'''
maze:  the input maze
ends:  the list of source and destination coordinates
steps: matrix that stores the minimum number of steps from
       the source coordinate to each visited maze cell.
       = -1 if the cell is part of a wall.
'''

# Read input maze
maze = []
ends = []
for r in range(10):
    maze.append(input())

# Set up the steps matrix
steps = [[0] * 10 for r in range(10)]
for r in range(10):
    for c in range(10):
        if maze[r][c] == '#':
            steps[r][c] = -1
        if maze[r][c] == 'X':
            ends.append((r, c))

# Breadth-First Search       
Queue = []
Queue.append((ends[0], 0))
visited = set()
while Queue != []:
    (r, c), dist = Queue.pop(0)

    if (r, c) == ends[1]:
        print("Output: ", dist)
        break
    for dr, dc in adj:
        rr, cc = r + dr, c + dc

        if not valid(rr, cc):
            continue
        if (rr, cc) in visited:
            continue

        visited.add((rr, cc))
        Queue.append(((rr, cc), dist+1))
