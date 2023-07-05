import math
import time

"""
input: 16 14 10 8 7 9 3 2 4 1
output:
    16     2^0
    14 10  2 ^ 1
    8 7 9 3   2  ^ 2
    2 4 1 _ _ _ _ _

(2 ^ 2)  + (2 ^ 1) + (2 ^ 0) = n

(2 ^ 0) + (2 ^ 1) + (2 ^ 2) + (2 ^ 3) + (2 ^ 4) = 31
(2 ^ 0) + (2 ^ 1) + (2 ^ 2) + (2 ^ 3) = 15
(2 ^ 0) + (2 ^ 1) + (2 ^ 2) = 7
(2 ^ 0) + (2 ^ 1) = 3
(2 ^ 0)  = 1

total element up to the height = (2 ** height)  - 1
                                 height = floor (log base 2 (total) + 1)

log (total + 1)
 n = 1    n  = 2     n = 4    n = 8   n  = 16
"""

# 16 14 10 8 7 9 3 2 4 1


"""
1. building a heap by inserting numbers
2. maximum or min; building a sorted list using the heap
"""

def has_parent(a_list, last_index):
    parent_index = last_index // 2
    if parent_index > 0:
        return [True, parent_index]
    return [False, None]


def swap(a_list, pos1, pos2):
    temp = a_list[pos1]
    a_list[pos1] = a_list[pos2]
    a_list[pos2] = temp


def has_child(a_list):
    # algorithm left = 2*i and right = 2*i + 1

    for index in range(len(a_list)):
        has_left = 2 * index
        has_right = (2 * index) + 1

        if has_left > len(a_list) - 1:
            a_list.append("_")
        elif has_right > len(a_list) - 1:
            a_list.append("_")


def debug():
    # has_child(A)

    i = 1
    j = 0
    while i < math.ceil(math.log(len(A) + 1, 2)) + 1:
        while j < (2 ** i) - 1 and j < len(A):
            print(A[j], end=" ")
            j += 1
        i += 1
        print()


def build_heap(a_list, number):
    insert(a_list, number)


def insert(a_list, number):
    a_list.append(number)
    last_index = len(a_list)

    is_parent_exist = True
    while is_parent_exist:
        is_parent_exist, parent_index = has_parent(a_list, last_index)

        if not is_parent_exist:
            break

        is_parent_exist, up_up_parent_index = has_parent(a_list, parent_index)

        if up_up_parent_index is not None:
            left_child_of_up_up_parent_index = up_up_parent_index * 2
            right_child_of_up_up_parent_index = (up_up_parent_index * 2) + 1
        else:
            root = parent_index
            left_child_of_up_up_parent_index = root
            right_child_of_up_up_parent_index = root

        if (
                a_list[left_child_of_up_up_parent_index - 1]
                < a_list[right_child_of_up_up_parent_index - 1]
        ):
            swap(a_list, last_index - 1, left_child_of_up_up_parent_index - 1)
            last_index = left_child_of_up_up_parent_index
        else:
            swap(a_list, last_index - 1, right_child_of_up_up_parent_index - 1)
            last_index = right_child_of_up_up_parent_index


st = time.process_time()
b = list(map(int, input().split()))
A = []
for i in range(len(b)):
    build_heap(A, b[i])
et = time.process_time()

debug()
print(A)

print(f"Running time: {et - st}")
