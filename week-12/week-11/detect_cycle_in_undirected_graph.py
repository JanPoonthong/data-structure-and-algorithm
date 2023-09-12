vertex, edge = map(int, input().split())


def read_input():
    data = [[] for i in range(vertex)]
    for i in range(edge):
        n1, n2, _ = input().split()
        n1 = int(n1)
        n2 = int(n2)

        data[n1].append(n2)

    return data

def dfs(graph, node):
    visited = []
    stack = []

    visited.append(node)
    stack.append(node)

    while stack:
        s = stack.pop()
        # print(s, end=" ")

        for n in reversed(graph[s]):
            if n not in visited:
                visited.append(n)
                stack.append(n)
    return visited


def check_connected(visited):
    miss = False
    for i in range(vertex):
        if i not in visited:
            miss = True

    if miss:
        print("UNCONNECTED")
    else:
        print("CONNECTED")


def main():
    adj_list = read_input()
    visited = dfs(adj_list, 0)

    check_connected(visited)

main()
