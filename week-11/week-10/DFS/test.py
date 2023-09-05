graph = {
    1: [2, 3],
    2: [],
    3: [2, 4],
    4: [3]
}

def dfs(graph, node):
    visited = []
    stack = []

    visited.append(node)
    stack.append(node) 

    while stack:
        s = stack.pop()
        print(s, end = " ")

        for n in reversed(graph[s]):
            if n not in visited:
                visited.append(n)
                stack.append(n)

def main():
    dfs(graph, 1)

main()
