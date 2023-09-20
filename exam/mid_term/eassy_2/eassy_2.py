import sys

sys.setrecursionlimit(10001)

root = None


class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.p = None
        self.left = None
        self.right = None


def Inorder_Tree_Walk(x):
    if x is not None:
        Inorder_Tree_Walk(x.left)
        print(x.key)
        Inorder_Tree_Walk(x.right)


def Tree_Minimum(x):
    while x.left is not None:
        x = x.left
    return x


def Tree_Maximum(x):
    while x.right is not None:
        x = x.right
    return x


def Tree_Successor(x):
    if x.right is not None:
        return Tree_Minimum(x.right)
    y = x.p
    while y is not None and x == y.right:
        x = y
        y = y.p
    return y


def Tree_Predecessor(x):
    if x.left is not None:
        return Tree_Maximum(x.left)
    y = x.p
    while y is not None and x == y.left:
        x = y
        y = y.p
    return y


"""
Adding your own Tree_Predecessor(x) is recommended, but not required
"""


def Transplant(u, v):
    global root

    if u.p is None:
        root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v

    if v is not None:
        v.p = u.p


def Tree_Delete(z):
    if z.left is None:
        Transplant(z, z.right)
    elif z.right is None:
        Transplant(z, z.left)
    else:
        y = Tree_Minimum(z.right)

        if y.p != z:
            Transplant(y, y.right)
            y.right = z.right
            y.right.p = y
        Transplant(z, y)
        y.left = z.left
        y.left.p = y


def Tree_Search(x, k):
    global root

    while x is not None and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x


def Tree_Insert(z):
    global root

    y = None
    x = root

    while x is not None:
        y = x

        if z.key < x.key:
            x = x.left
        else:
            x = x.right

    z.p = y
    if y is None:
        root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z


# Function to print
def printCall(node, indent, last):
    if node is not None:
        print(indent, end=" ")
        if last:
            print("R----", end=" ")
            indent += "     "
        else:
            print("L----", end=" ")
            indent += "|    "

        print(str(node.key))
        printCall(node.left, indent, False)
        printCall(node.right, indent, True)


# Function to call print
def print_BSTree(root):
    printCall(root, "", True)


def main():
    key_list = [56, 70, 30, 60, 65, 22, 11, 16, 40, 95, 63, 3, 67]
    for i in range(len(key_list)):
        Tree_Insert(Node(key_list[i]))

    print_BSTree(root)

    print(Tree_Predecessor(Tree_Search(root, 63)).key)
    print(Tree_Successor(Tree_Search(root, 67)).key)

    Tree_Delete(Tree_Search(root, 40))

    print_BSTree(root)


main()
