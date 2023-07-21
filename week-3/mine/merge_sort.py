import time

data = list(map(int, input().split()))


def merge(int_list, left_list, right_list):
    i = 0
    j = 0
    k = 0

    while i < len(left_list) and j < len(right_list):
        if left_list[i] > right_list[j]:
            int_list[k] = right_list[j]
            j += 1
        else:
            int_list[k] = left_list[i]
            i += 1
        k += 1

    while i < len(left_list):
        int_list[k] = left_list[i]
        i += 1
        k += 1

    while j < len(right_list):
        int_list[k] = right_list[j]
        j += 1
        k += 1


def merge_sort(int_list):
    if len(int_list) > 1:
        mid_point = len(int_list) // 2
        left_list = int_list[:mid_point]
        right_list = int_list[mid_point:]

        merge_sort(left_list)
        merge_sort(right_list)
        merge(int_list, left_list, right_list)


st = time.process_time()

merge_sort(data)

et = time.process_time()

print(data)
print(et - st)

is_sorted = data == sorted(data)
print(is_sorted)
