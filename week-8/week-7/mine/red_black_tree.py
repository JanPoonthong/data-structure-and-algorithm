from collections import deque

RED = 1
BLACK = 0

class Node:
    def __init__(self, key, data=None):
        self.data = data
        self.key = key
        self.p = None
        self.left = None
        self.right = None
        self.color = RED


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(0)
        self.NIL.color = BLACK
        self.NIL.left = None
        self.NIL.right = None
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left 


        if y.left != self.NIL:
            y.left.p = x
        
        y.p = x.p

        if x.p is None:
            self.root = y
        # TODO(jan): Understand the code
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y

        y.left = x
        x.p = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right

        if y.right is not self.NIL:
            y.right.p = x

        y.p = x.p

        if x.p is None:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y

        y.right = x
        x.p = y

    def insert(self, key):
        z = Node(key)
        z.left = self.NIL
        z.right = self.NIL

        y = None
        x = self.root

        while x != self.NIL:
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

        self.insert_fixup(z)

    def insert_fixup(self, z):
        while z.p and z.p.color == RED:
            # case 1; if z.uncle == RED
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == RED:
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.left_rotate(z)
                    z.p.color = BLACK
                    z.p.p.color = RED
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color == RED:
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = BLACK
                    z.p.p.color = RED
                    self.left_rotate(z.p.p)

            if z == self.root:
                break

        self.root.color = BLACK

    def search(self, k):
        x = self.root
        while x != self.NIL and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def print_tree(self, val="key", left="left", right="right"):
        root = self.root
        visited = set()

        def display(root, val=val, left=left, right=right):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            s_color = "RED" if root.color == 1 else "BLACK"

            if root is not self.NIL:
                if root in visited:
                    line = "***%s(%s)***" % (getattr(root, val), s_color)
                    width = len(line)
                    height = 1
                    middle = width // 2
                    return [line], width, height, middle
                visited.add(root)

            if getattr(root, right) is None and getattr(root, left) is None:
                line = "%s(%s)" % (getattr(root, val), s_color)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if getattr(root, right) is None:
                lines, n, p, x = display(getattr(root, left))
                s = "%s" % getattr(root, val)
                u = len(s)
                first_line = (x + 1) * " " + (n - x - 1) * "_" + s
                second_line = x * " " + "/" + (n - x - 1 + u) * " "
                shifted_lines = [line + u * " " for line in lines]
                return (
                    [first_line, second_line] + shifted_lines,
                    n + u,
                    p + 2,
                    n + u // 2,
                )

            # Only right child.
            if getattr(root, left) is None:
                lines, n, p, x = display(getattr(root, right))
                s = "%s" % getattr(root, val)
                u = len(s)
                first_line = s + x * "_" + (n - x) * " "
                second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
                shifted_lines = [u * " " + line for line in lines]
                return (
                    [first_line, second_line] + shifted_lines,
                    n + u,
                    p + 2,
                    u // 2,
                )

            # Two children.
            left, n, p, x = display(getattr(root, left))
            right, m, q, y = display(getattr(root, right))
            s = "%s(%s)" % (getattr(root, val), s_color)
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
            second_line = x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
            if p < q:
                left += [n * " "] * (q - p)
            elif q < p:
                right += [m * " "] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        lines, *_ = display(root, val, left, right)
        for line in lines:
            print(line)
        print("---------------------------------------------------------------")


def main():
    red_black_tree = RedBlackTree()
    data = [10, 1, 5, 2, 3]
    for i in data:
        red_black_tree.insert(i)

    red_black_tree.print_tree()
    searched_node = red_black_tree.search(2)




main()
