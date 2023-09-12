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

visited = []
queue = []
node = 0
visited.append(node)
queue.append(node)
time = time + 1
d[node] = time

track = []

while queue:
    s = queue.pop()
    track.append(s)

    for n in reversed(adj_list[s]):
        if n not in visited:
            visited.append(n)
            queue.append(n)
            p[n] = s
            time = time + 1
            d[n] = time

            if adj_list[n] == []:
                time = time + 1
                f[n] = time

for i in reversed(track):
    if f[i] == -1:
        time = time + 1
        f[i] = time

print()
print_call()
