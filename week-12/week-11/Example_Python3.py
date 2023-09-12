# Python 3 class


class item:
    def __init__(self):
        self.p = None


x = [None] * 5
for i in range(5):
    x[i] = item()
    x[i].index = i
    x[i].key = i + 10
for i in range(5):
    print(x[i].index, x[i].key, x[i].p)

# -------------------------------------

# Python 3 tuple

y = []
for i in range(5):
    y.append((i, i * 2, i * 3))
print(y)

# -------------------------------------

# Sorting x based on the key value of each item


def itemKey(a):
    return a.key


x.sort(key=itemKey, reverse=True)
for i in range(5):
    print(x[i].index, x[i].key, x[i].p)

# -------------------------------------

# Sorting y based on the 3rd element of each tuple


def tupleKey(a):
    return a[2]


y.sort(key=tupleKey, reverse=True)
print(y)
