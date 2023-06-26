import time

k = int(input(""))
input_list = input("").split(" ")

my_list = []
for i in input_list:
    if i.isnumeric():
        my_list.append(int(i))


start_time = time.process_time()
found = False
for i in range(len(my_list)):
    for j in range(len(my_list)):
        if int(my_list[i]) * int(my_list[j]) == k:
            print(my_list[i], my_list[j])
            found = True
            break
if not found:
    print("no pair exists")

end_time = time.process_time()
print(end_time - start_time)
