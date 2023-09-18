"""
Python 3
A explicit comparing function is required for custom priority definition
The compare function takes two items:
  - returns True if the first item has higher priority than the second
  - returns False otherwise
The function is to be passed to the heap instantiation
"""


class Heap:
    def compare(x, y):  # a default compare function for min heap
        return x < y

    def empty(self):
        if self.heapsize == 0:
            return True
        else:
            return False

    def heapify(self, i):
        l = i * 2 + 1
        r = (i + 1) * 2
        if l < self.heapsize and self.cmp(self.a[l], self.a[i]):
            largest = l
        else:
            largest = i
        if r < self.heapsize and self.cmp(self.a[r], self.a[largest]):
            largest = r
        if largest != i:
            self.a[i], self.a[largest] = self.a[largest], self.a[i]
            self.heapify(largest)

    def insert(self, x):
        self.heapsize += 1
        if len(self.a) < self.heapsize:
            self.a.append(x)
        else:
            self.a[self.heapsize - 1] = x
        i = self.heapsize - 1
        j = (i - 1) // 2
        while i > 0 and self.cmp(self.a[i], self.a[j]):
            self.a[i], self.a[j] = self.a[j], self.a[i]
            i = j
            j = (i - 1) // 2

    def extract(self):
        x = self.a[0]
        last = self.heapsize - 1
        self.a[0], self.a[last] = self.a[last], self.a[0]
        self.heapsize -= 1
        self.heapify(0)
        return x

    def buildHeap(self):
        for i in range((self.heapsize - 1) // 2, -1, -1):
            self.heapify(i)

    def __init__(self, items=[], cmp=compare):
        self.a = items
        self.cmp = cmp
        self.heapsize = len(self.a)
        if len(self.a) > 0:
            self.buildHeap()


def myCompare(x, y):  # max heap
    return x.key > y.key


class myClass:
    def __init__(self, k):
        self.key = k

"""
testList = [i + 100 for i in range(10)]

pq1 = Heap(items=testList)  # default as min heap for a list of numbers
pq2 = Heap(cmp=myCompare)  # custom class item with custom compare function

for v in testList:
    pq2.insert(myClass(v))

while not pq1.empty():
    print(pq1.extract(), end=" ")
print()

while not pq2.empty():
    print(pq2.extract().key, end=" ")

"""

def read_input():
    vertex, edge = map(int, input().split())

    data = {}
    for i in range(1, vertex+1):
        data[i] = []

    for i in range(edge):
        node_one, node_two, weight = map(int, input().split())

        if node_one in data:
            data[node_one].append((node_two, weight))
        else:
            data[node_one] = [(node_two, weight)]

    return data, vertex

class myClass:
    def __init__(self, short, start):
        self.short = short
        self.start = start

def myCompare(x, y):
    return x.short < y.short


def diskstra_heap(data, vertex):
    shortest_paths = {}
    start = 1
    visited = {}
    for i in range(start, vertex+1):
        visited[i] = False
        shortest_paths[i] = float("inf")

    for node in list(data.keys()):
        shortest_paths[node] = float("inf")
        visited[node] = False

    shortest_paths[start] = 0
    visited[start] = True

    heap = Heap(cmp=myCompare)

    heap.insert(myClass(0, 1))

    while heap.heapsize > 0:
        a = heap.extract()

        (distance, node) = a.short, a.start
        visited[node] = True

        for edge in data[node]:
            cost = edge[1]
            to_node = edge[0]

            if (not visited[to_node]) and (distance + cost < shortest_paths[to_node]):
                shortest_paths[to_node] = distance + cost
                heap.insert(myClass(shortest_paths[to_node], to_node))

    return shortest_paths

def main():
    data, vertex = read_input()
    shortest_paths = diskstra_heap(data, vertex)
    print(shortest_paths[list(shortest_paths)[-1]])


main()
