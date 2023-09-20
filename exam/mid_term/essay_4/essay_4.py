import time


class heap:
    def compare(x, y):  # a default compare function for min heap
        return x > y

    def empty(self):
        if self.heapsize == 0:
            return True
        else:
            return False

    def heapify(self, i):
        self.count += 1
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
        self.count = 0
        if len(self.a) > 0:
            self.buildHeap()


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

st = time.process_time()
h = heap(items=A)

print(h.count)

et = time.process_time()
