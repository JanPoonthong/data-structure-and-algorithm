graph_type = input()
if graph_type != "Directed Graph":
    print("DFS only works on Directed Graph")
    exit()

V,E = map(int, input().split())

adj_list = [[] for v in range(V)]
for i in range(E):
    u,v = map(int, input().split())
    u -= 1
    v -= 1 # why? somewhat easier to write for loop and stuff
    adj_list[u].append(v)
    # at index 1-1=0, we have 2-1=1
    # at index 2-1=1, we have 4-1=3
    # at index 3-1=2, we have 4-1=3
    # at index 2-1=1, we have 1-1=0
    # at index 3-1=2, we have 3-1=2
    print(f"Adjacent List: {adj_list}")

color = ["WHITE"]*V
p = [None]*V
time = 0
d = [-1]*V
f = [-1]*V

# Write your Depth-First Search code below
# Don't forget to make the initial dfs call! :)
time = 0

def dfs_visit(u):
    global time, d
    time += 1
    d[u] = time
    color[u] = "GREY"               # mark u as visited
    print(u+1)

    for v in adj_list[u]:
        if color[v] == "WHITE":     # if v is unvisited
            p[v] = u                # mark parent of the v as u
            dfs_visit(v)            # dfs-visit v

    color[u] = "BLACK"              # mark u as explored
    time += 1                       # increment time
    f[u] = time                     # store the time at u's finish_time


for u in range(V):
    if color[u] == "WHITE":         # dfs-visit for every unvisited u
        dfs_visit(u)




# The code below is for printing output

for v in range(V):
    if d[v] == -1:
        dv = "undiscovered"
    else:
        dv = d[v]
    if f[v] == -1:
        fv = ""
    else:
        fv = f[v]
    if p[v] != None:
        pv = p[v]+1
    else:
        pv = "None"

    print((v+1, color[v]), dv, fv, pv)

