graph_type = input()
V,E = map(int, input().split())
adj_list = [[] for v in range(V)]
for i in range(E):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    adj_list[u].append(v)
    if graph_type == "Undirected Graph":
        adj_list[v].append(u)

color = ["WHITE"]*V
d = [-1]*V
p = [None]*V

# Write your Breast-First Search code below

for node in range(V):
    if color[node] == "WHITE":
        color[node] = "GRAY"
        d[node] = 0
        p[node] = None

    queue = [node]

    while len(queue) > 0:
        parent = queue.pop(0)
        for neighbor in adj_list[parent]:
            if color[neighbor] == "WHITE":
                color[neighbor] = "GRAY"
                d[neighbor] = d[parent] + 1
                p[neighbor] = parent
                queue.append(neighbor)

        color[parent] = "BLACK"

# The code below is for printing output

for v in range(V):
    if d[v] == -1:
        dv = "Inf"
    else:
        dv = d[v]
    if p[v] != None:
        pv = p[v]+1
    else:
        pv = "None"

    print("%d %5s" % (v+1, color[v]), dv, pv)

