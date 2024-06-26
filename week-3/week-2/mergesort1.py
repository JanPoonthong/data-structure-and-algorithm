import time


def merge(A, p, q, r):
    B = []
    i = p
    j = q + 1
    while i <= q and j <= r:
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1
    A[p : r + 1] = B + A[i : q + 1] + A[j : r + 1]


def mergesort(A, p, r):
    if len(A) > 1:
        middle = len(A) // 2
        left = A[:middle]
        right = A[middle:]

        mergesort(left, 0, len(A) - 1)
        mergesort(right, 0, len(A) - 1)
        merge(A, len(left), 0, len(right))


a = list(map(int, input().split()))

st = time.process_time()

mergesort(a, 0, len(a) - 1)

et = time.process_time()

print(a)
print(et - st)
