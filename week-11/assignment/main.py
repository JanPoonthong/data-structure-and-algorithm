vertex = int(input())
adj_list = [[] for v in range(vertex)]

for i in range(vertex):
    list_of_adj_list = list(map(int, input().split()))
    node = list_of_adj_list[0] - 1
    edge = list_of_adj_list[1] - 1
    edge_list = list_of_adj_list[2:]
    for j in edge_list:
        adj_list[node].append(j)

a = [[] for v in range(len(adj_list))]
for x in range(len(adj_list)):
    for i in adj_list[x]:
        a[x].append(i - 1)


color = ["WHITE"] * vertex
d = [-1] * vertex

node = 0
if color[node] == "WHITE":
    color[node] = "GRAY"
    d[node] = 0

queue = [node]

while len(queue) > 0:
    parent = queue.pop(0)
    for neighbor in a[parent]:
        if color[neighbor] == "WHITE":
            color[neighbor] = "GRAY"
            d[neighbor] = d[parent] + 1
            queue.append(neighbor)

    color[parent] = "BLACK"

def debug():
    for v in range(vertex):
        if d[v] == -1:
            dv = -1
        else:
            dv = d[v]
        print("%d %d" % (v + 1, dv))

debug()
