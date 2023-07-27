import time


class Heap:
    def __init__(self, items=None):
        self.a = items[:] if items is not None else []
        self.heap_size = len(self.a)
        self.build_heap()

    @staticmethod
    def compare(x, y):
        return x < y

    def empty(self):
        return self.heap_size == 0

    def heapify_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.compare(self.a[i], self.a[parent]):
                self.a[i], self.a[parent] = self.a[parent], self.a[i]
                i = parent
            else:
                break

    def heapify_down(self, i):
        while True:
            smallest = i
            left_child = 2 * i + 1
            right_child = 2 * i + 2

            if left_child < self.heap_size and self.compare(
                self.a[left_child], self.a[smallest]
            ):
                smallest = left_child

            if right_child < self.heap_size and self.compare(
                self.a[right_child], self.a[smallest]
            ):
                smallest = right_child

            if smallest == i:
                break

            self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
            i = smallest

    def insert(self, x):
        self.heap_size += 1
        if len(self.a) < self.heap_size:
            self.a.append(x)
        else:
            self.a[self.heap_size - 1] = x
        self.heapify_up(self.heap_size - 1)

    def extract(self):
        if self.empty():
            raise ValueError("Error: Heap is empty")
        x = self.a[0]
        self.a[0] = self.a[self.heap_size - 1]
        self.heap_size -= 1
        self.heapify_down(0)
        return x

    def build_heap(self):
        for i in range(self.heap_size // 2 - 1, -1, -1):
            self.heapify_down(i)


A = list(map(int, input().split()))

st = time.process_time()
h = Heap(items=A)

total = 0
while h.heap_size > 1:
    first = h.extract()
    second = h.extract()
    temp = first + second
    total += temp
    h.insert(temp)

et = time.process_time()

print(total)
