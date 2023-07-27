# ---- BS Tree -----

"""
from BinarySearchTree import *

bst = BSTree()
a = [4, 5, 12, -5, -87, 9, 1023]

import random

random.shuffle(a)

for k in a:
    x = BST_Node(k)
    bst.Tree_Insert(x)
    
bst.print_BSTree()
"""
"""
bst2 = BSTree()
for k in range(1,11):
    x = BST_Node(k)
    bst2.Tree_Insert(x)

bst2.print_BSTree()
"""
# ---- RB Tree -----

from RedBlackTree import *

rbt = RBTree()
a = [8, 6, 4, 5, 3]
for k in a:
    x = RB_Node(k)
    rbt.RB_Insert(x)
rbt.print_RBTree()

k = len(a) // 2
