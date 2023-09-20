A = list(map(str, input().split()))
B = list(map(str, input().split()))

# Test case 1
# A B C D E F G H
# A B C A

# Test 2
# K A M W P Z
# K P Z A

# Test 3
# R V B 4 C R R R
# R V B R

dictA = {}
dictB = {}

for i in range(len(A)):
    dictA.setdefault(A[i], A.count(A[i]))

for j in range(len(B)):
    dictB.setdefault(B[j], B.count(B[j]))
print(dictA)
print(dictB)

for i in B:
    if dictB.get(i) <= dictA.get(i):
        print("Yes")
        break
    else:
        print("No")
        break
