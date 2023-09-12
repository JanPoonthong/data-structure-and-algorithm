V, E = map(int, input().split())
edgeList = []
for i in range(E):
    edgeList.append(tuple(map(int, input().split())))

print(edgeList)

from disjointsets3 import DisjointSets

s = DisjointSets(V)

for i in range(V):
    for j in edgeList:
        if j[0] == i:
            s.union(j[0], j[1])

miss = False
for i in range(V-1):
    if s.findset(i) != s.findset(i+1):
        miss = True


if miss:
    print("UNCONNECTED")
else:
    print("CONNECTED")
