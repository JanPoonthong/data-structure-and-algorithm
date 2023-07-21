class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


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
            self.remove_node(node)
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

    def remove_node(self, node):
        if node.left is None and node.right is None:
            self.transplant(node, None)
        elif node.left is not None and node.right is not None:
            successor = self.successor(node)
            node.data = successor.data
            self.remove_node(successor)
        else:
            child = node.left if node.left else node.right
            self.transplant(node, child)

    def transplant(self, target, new_node):
        if target.parent is None:
            self.root = new_node
        elif target == target.parent.left:
            target.parent.left = new_node
        else:
            target.parent.right = new_node

        if new_node is not None:
            new_node.parent = target.parent

    def successor(self, node):
        current = node.right
        while current.left is not None:
            current = current.left
        return current

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            self.insert_helper(self.root, new_node)

    def insert_helper(self, node, new_node):
        if new_node.data < node.data:
            if node.left is None:
                node.left = new_node
                new_node.parent = node
            else:
                self.insert_helper(node.left, new_node)
        else:
            if node.right is None:
                node.right = new_node
                new_node.parent = node
            else:
                self.insert_helper(node.right, new_node)

    def display(self):
        self.display_helper(self.root)

    def display_helper(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.data))
            self.display_helper(node.left, level + 1, "L---- ")
            self.display_helper(node.right, level + 1, "R---- ")

    def print_tree(self):
        self.display()


def main():
    tree = BinarySearchTree()
    data_list = [4, 2, 1, 6, 5, 7, 3]
    for data in data_list:
        tree.insert(data)

    search_key = 1
    print(f"Search {search_key}: {tree.search(search_key)}")

    remove_key = 6
    tree.remove(remove_key)

    tree.print_tree()


main()
