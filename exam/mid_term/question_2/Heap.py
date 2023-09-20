"""
Python 3
A explicit comparing function is required for custom priority definition
The compare function takes two items:
  - returns True if the first item has higher priority than the second
  - returns False otherwise
The function is to be passed to the heap instantiation
"""


class heap:
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


# Example class definition for heap's element and test code

"""
def myCompare(x, y):  # max heap
    return x.key > y.key


class myClass:
    def __init__(self, k):
        self.key = k


testList = [i + 100 for i in range(10)]

pq1 = heap(items=testList)  # default as min heap for a list of numbers
pq2 = heap(cmp=myCompare)  # custom class item with custom compare function

for v in testList:
    pq2.insert(myClass(v))

while not pq1.empty():
    print(pq1.extract(), end=" ")
print()

while not pq2.empty():
    print(pq2.extract().key, end=" ")
"""
