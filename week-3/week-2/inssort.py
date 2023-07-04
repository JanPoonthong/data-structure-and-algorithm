import time

a = list(map(int, input().split()))

n = len(a)

st = time.process_time()


def insertion_sort(my_list, len_n):
    for i in range(1, len_n):
        key = my_list[i]
        j = i - 1

        while j >= 0 and key < my_list[j]:
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = key


insertion_sort(a, n)

et = time.process_time()

print(a)
print(et - st)
