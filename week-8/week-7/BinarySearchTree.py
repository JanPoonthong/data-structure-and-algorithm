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

def main():
    tree = BSTree()
    key_list = [4, 2, 1, 6, 5, 7, 3]
    data_list = [
        "Hello",
        "World",
        "Programmer",
        "New",
        "Jan",
        "Ton",
        "Something",
    ]
    for i in range(len(key_list)):
        tree.Tree_Insert(BST_Node(key_list[i], data_list[i]))

    search_key = 1
    search_node = tree.Tree_Search(search_key)
    if search_node:
        print(f"Search {search_key}: {search_node.data}")
    else:
        print(f"Search {search_key}: Not Found")

    remove_key = 9
    to_remove_search_node = tree.Tree_Search(remove_key)
    if to_remove_search_node:
        tree.Tree_Delete(to_remove_search_node)
    else:
        print(f"Removing {remove_key} not found")

    tree.print_BSTree()

main()
