K = int(input())
a = list(map(int, input().split()))

import time

st = time.process_time()

found = False
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i]*a[j] == K:
            found = True
            break
    if found:
        break

et = time.process_time()

if not found:
    print("no pair exists")
else:
    print(a[i], a[j])
print("running time:", et-st)

