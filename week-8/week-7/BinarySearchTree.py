import sys

sys.setrecursionlimit(10001)


class BST_Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.p = None
        self.left = None
        self.right = None


class BSTree:
    def __init__(self):
        self.root = None

    def Tree_Maximum(self, x):
        while x.right is not None:
            x = x.right
        return x

    def Tree_Minimum(self, x):
        while x.left is not None:
            x = x.left
        return x

    def Transplant(self, u, v):
        if u.p is None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v is not None:
            v.p = u.p

    def Tree_Delete(self, z):
        if z.left is None:
            self.Transplant(z, z.right)
        elif z.right is None:
            self.Transplant(z, z.left)
        else:
            y = self.Tree_Minimum(z.right)
            if y.p != z:
                self.Transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.Transplant(z, y)
            y.left = z.left
            y.left.p = y

    def Tree_Insert(self, z):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def Tree_Successor(self, x):
        if x.right is not None:
            return self.Tree_Minimum(x.right)
        y = x.p
        while y is not None and x == y.right:
            x = y
            y = y.p
        return y

    def Tree_Predecessor(self, x):
        if x.left is not None:
            return self.Tree_Maximum(x.left)
        y = x.p
        while y is not None and x == y.left:
            x = y

    def Tree_Search(self, k):
        x = self.root
        while x is not None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def Inorder_Tree_Walk(self, x):
        if x is not None:
            self.Inorder_Tree_Walk(x.left)
            print(x.key)
            self.Inorder_Tree_Walk(x.right)

    # Function to print
    def __printCall(self, node, indent, last):
        if node is not None:
            print(indent, end=" ")
            if last:
                print("R----", end=" ")
                indent += "     "
            else:
                print("L----", end=" ")
                indent += "|    "

            print(str(node.key))
            self.__printCall(node.left, indent, False)
            self.__printCall(node.right, indent, True)

    # Function to call print
    def print_BSTree(self):
        self.__printCall(self.root, "", True)
