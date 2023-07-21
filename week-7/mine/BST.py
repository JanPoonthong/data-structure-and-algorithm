class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, data):
        return self.search_helper(self.root, data)

    def search_helper(self, node, data):
        if node is None:
            return False
        elif node.data == data:
            return True
        elif data < node.data:
            return self.search_helper(node.left, data)
        else:
            return self.search_helper(node.right, data)

    def remove(self, data):
        node = self.find_node(self.root, data)
        if node:
            print(f"Removed {data}")
            self.remove_helper(self.root, data)
        else:
            print(f"{data} could not be found")

    def find_node(self, node, data):
        if node is None:
            return None
        elif node.data == data:
            return node
        elif data < node.data:
            return self.find_node(node.left, data)
        else:
            return self.find_node(node.right, data)



    def remove_helper(self, root, data):
        if root is None:
            return root
        elif data < root.data:
            root.left = self.remove_helper(root.left, data)
        elif data > root.data:
            root.right = self.remove_helper(root.right, data)
        # node found
        else:
            # leaf node
            if root.left is None and root.right is None:
                root = None
            elif root.right is not None:
                root.data = self.successor(root)
                root.right = self.remove_helper(root.right, root.data)
            elif root.left is not None:
                root.data = self.predecessor(root)
                root.left = self.remove_helper(root.left, root.data)

        return root

    @staticmethod
    def successor(root):
        root = root.right
        while root.left is not None:
            root = root.left
        return root.data

    @staticmethod
    def predecessor(root):
        root = root.left
        while root.right is not None:
            root = root.right
        return root.data
        pass

    def display(self):
        self.display_helper(self.root)

    def display_helper(self, root):
        if root is not None:
            self.display_helper(root.left)
            print(root.data)
            self.display_helper(root.right)

    def insert(self, node):
        self.root = self.insert_helper(self.root, node)

    def insert_helper(self, root, node):
        if root is None:
            return node

        if node.data < root.data:
            root.left = self.insert_helper(root.left, node)
        else:
            root.right = self.insert_helper(root.right, node)

        return root

    def print_call(self, node, indent, last):
        if node is not None:
            print(indent, end=" ")
            if last:
                print("R----", end=" ")
                indent += "     "
            else:
                print("L----", end=" ")
                indent += "|    "

            print(str(node.data))
            self.print_call(node.left, indent, False)
            self.print_call(node.right, indent, True)

    def print_tree(self):
        self.print_call(self.root, "", True)


def main():
    tree = BinarySearchTree()
    data_list = [4, 2, 1, 6, 5, 7, 3]
    for data in data_list:
        tree.insert(Node(data))

    search_key = 1
    print(f"Search {search_key}: {tree.search(search_key)}")

    remove_key = 6
    tree.remove(remove_key)

    tree.print_tree()


main()
