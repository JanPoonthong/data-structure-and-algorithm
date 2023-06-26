K = int(input())
a = list(map(int, input().split()))

import time

st = time.process_time()

found = False
for x in a:
    y = K/x
    if y != x:
        for z in a:
            if z == y:
                found = True
                break
    if found:
        break

et = time.process_time()

if not found:
    print("no pair exists")
else:
    print(x, int(y))
print("running time:", et-st)

