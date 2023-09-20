from Heap import heap
import time

A = list(map(int, input().split()))

n = len(A)


def checkout_max(a):
    global h
    return h.extract()


def max_compare(x, y):
    return x > y


st = time.process_time()
h = heap(items=A, cmp=max_compare)

for i in range(n - 1, -1, -1):
    A[i] = checkout_max(A)

et = time.process_time()

print(A)
print(et - st)
