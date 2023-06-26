import time

K = int(input())
a = list(map(int, input().split()))

st = time.process_time()

a.sort()

def BinSrch(key, p, r):
    while p <= r:
        q = (p+r)//2
        if a[q] == key:
            return True, q
        elif key < a[q]:
            r = q-1
        else:
            p = q+1
    return False, -1
    

found = False
for x in a:
    y = K/x
    found, j = BinSrch(y, 0, len(a)-1)
    if found:
        break

et = time.process_time()

if not found:
    print('No pair multiplies to k')
else:
    print(x,int(y))

print(et-st)
