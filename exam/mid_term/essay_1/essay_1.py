import time


def partition(a, p, r):  # Lomuto's partition scheme
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[r], a[i + 1] = a[i + 1], a[r]
    return i + 1


def quick_sort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        print(A[p:q], A[q], A[q + 1 : r + 1])
        quick_sort(a, p, q - 1)  # left side
        quick_sort(a, q + 1, r)  # right side


A = list(map(int, input().split()))

st = time.process_time()
quick_sort(A, 0, len(A) - 1)
et = time.process_time()

print(et - st)
