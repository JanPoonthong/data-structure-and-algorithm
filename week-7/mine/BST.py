class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, key):
        return self.search_helper(self.root, key)

    def search_helper(self, node, key):
        if node is None:
            return False
        elif node.key == key:
            return node
        elif key < node.key:
            return self.search_helper(node.left, key)
        else:
            return self.search_helper(node.right, key)

    def remove(self, key):
        node = self.find_node(self.root, key)
        if node:
            print(f"Removed {key}")
            self.remove_helper(self.root, key)
        else:
            print(f"{key} could not be found")

    def find_node(self, node, key):
        if node is None:
            return None
        elif node.key == key:
            return node
        elif key < node.key:
            return self.find_node(node.left, key)
        else:
            return self.find_node(node.right, key)

    def remove_helper(self, root, key):
        if root is None:
            return root
        elif key < root.key:
            root.left = self.remove_helper(root.left, key)
        elif key > root.key:
            root.right = self.remove_helper(root.right, key)
        # node found
        else:
            # leaf node
            if root.left is None and root.right is None:
                root = None
            elif root.right is not None:
                root.key = self.successor(root)
                root.right = self.remove_helper(root.right, root.key)
            elif root.left is not None:
                root.key = self.predecessor(root)
                root.left = self.remove_helper(root.left, root.key)

        return root

    @staticmethod
    def successor(node):
        current = node.right
        while current.left is not None:
            current = current.left
        return current.key

    @staticmethod
    def predecessor(root):
        root = root.left
        while root.right is not None:
            root = root.right
        return root.key
        pass

    def insert(self, node):
        self.root = self.insert_helper(self.root, node)

    def insert_helper(self, root, node):
        if root is None:
            return node

        if node.key < root.key:
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

            print(str(node.key))
            self.print_call(node.left, indent, False)
            self.print_call(node.right, indent, True)

    def print_tree(self):
        self.print_call(self.root, "", True)


def main():
    tree = BinarySearchTree()
    key_list = [4, 2, 1, 6, 5, 7, 3]
    data_list = ["Hello", "World", "Programmer", "New", "Jan", "Ton",
                 "Something"]
    for i in range(len(key_list)):
        tree.insert(Node(key_list[i], data_list[i]))

    search_key = 1
    search_node = tree.search(search_key)
    print(f"Search {search_key}: {search_node.data}")

    remove_key = 6
    tree.remove(remove_key)

    tree.print_tree()


main()
