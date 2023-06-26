import time


def mergesort(a):
    if len(a) > 1:

        middle_point = len(a) // 2
        left = a[:middle_point]
        right = a[middle_point:]

        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[i]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[i]
                j += 1
            k += 1


a = list(map(int, input().split()))
st = time.process_time()

mergesort(a)

et = time.process_time()

print(a)
# print(et - st)
