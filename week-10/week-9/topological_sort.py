# A call to topological_sort must be with two arguments
# 1) The number of vertices of the Directed Acyclic Graph
# 2) The adjacency list of the graph

visited = []
stack = []


def DFS_visit(s, adj):
    global visited, stack

    for v in adj[s]:
        if not visited[v]:
            visited[v] = True
            DFS_visit(v, adj)
    stack.append(s)


def topological_sort(V, adj):
    global visited, stack

    visited = [False] * V
    for s in range(V):
        if not visited[s]:
            visited[s] = True
            DFS_visit(s, adj)
    stack.reverse()
    return stack
