import time


def merge(A, p, q, r):
    # merge the sorted A[p:q+1] with the sorted A[q+1:r+1]
    # the result is a sorted A[p:r+1]
    # Hint: an auxiliary list is required
    # Complete the body of this function
    pass


def mergesort(A, p, r):
    # Complete the body of this function
    if len(A) > 1:

        middle_point = len(A) // 2
        left = a[:middle_point]
        right = a[middle_point:]

        mergesort(left, 0, len(a) - 1)
        mergesort(right, 0, len(a) - 1)


a = list(map(int, input().split()))
st = time.process_time()

mergesort(a, 0, len(a) - 1)

et = time.process_time()

print(a)
# print(et - st)
