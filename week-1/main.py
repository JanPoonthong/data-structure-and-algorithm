n = int(input(""))
for i in range(1, n + 1):
    print(i)

list_of_integer = [int(i) for i in input("").split(" ")]
print(list_of_integer)


odd_numbers = (str(i) for i in list_of_integer if i % 2 == 1)
print(" ".join(odd_numbers))

largest_odd = 0
for i in list_of_integer:
    if i % 2 == 1 and i > largest_odd:
        largest_odd = i

print(largest_odd)

i = len(list_of_integer) - 1
while i >= 0:
    if list_of_integer[i] % 2 == 0:
        print(list_of_integer[i], end=" ")
    i -= 1

print()
