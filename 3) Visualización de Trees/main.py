from AVL_tree import AVL_tree
import random

N = 100

data_avl = random.sample(range(1, 101), N)

tree = AVL_tree()

for data in data_avl:
    tree.insert(data)

print(tree._traverse(tree.root))
print('Current root: {}'.format(tree.root)) 

tree.visualize()