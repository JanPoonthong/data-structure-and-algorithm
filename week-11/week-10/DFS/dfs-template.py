graph_type = input()
if graph_type != "Directed Graph":
    print("DFS only works on Directed Graph")
    exit()

V, E = map(int, input().split())
adj_list = [[] for v in range(V)]
for i in range(E):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj_list[u].append(v)

color = ["WHITE"] * V
p = [None] * V
time = 0
d = [-1] * V
f = [-1] * V


def print_call():
    for v in range(V):
        if d[v] == -1:
            dv = "undiscovered"
        else:
            dv = d[v]
        if f[v] == -1:
            fv = ""
        else:
            fv = f[v]
        if p[v] is not None:
            pv = p[v] + 1
        else:
            pv = "None"

        print("%d %5s" % (v + 1, color[v]), dv, fv, pv)

# [[1, 2], [], [1, 3], [2]]


def dfs_visit(vertex):
    global time, d
    time += 1
    d[vertex] = time
    color[vertex] = "GREY"               # mark u as visited

    for vertex_inside_adj in adj_list[vertex]:
        if color[vertex_inside_adj] == "WHITE":     # if v is unvisited
            p[vertex_inside_adj] = vertex           # mark parent of the v as u
            dfs_visit(vertex_inside_adj)            # dfs-visit v

    color[vertex] = "BLACK"              # mark u as explored
    time += 1                            # increment time
    f[vertex] = time                     # store the time at u's finish_time


for each_vertex in range(V):
    if color[each_vertex] == "WHITE":         # dfs-visit for every unvisited u
        dfs_visit(each_vertex)

print_call()
