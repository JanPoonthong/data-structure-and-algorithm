import time

a = list(map(int, input().split()))

n = len(a)

st = time.process_time()


# write the insertion sort code into this segment
def inssort(a, n):
    for i in range(1, n):
        # starting at the 2 index
        temp = a[i]
        # left of i
        j = i - 1

        # check number on the left
        while j >= 0 and a[j] > temp:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = temp


# 3 30 20 42 1R

# 3 30 30 42 1


inssort(a, n)

et = time.process_time()

print(a)
print(et - st)
