from AVL_tree import AVL_tree


tree = AVL_tree()

print('AVL object: {}'.format(tree)) 
print('Current root: {}'.format(tree.root)) 

nodes_data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for data in nodes_data:
    tree.insert(data)
    
print('Current root: {}'.format(tree.root))

print('Searching for {}: {}'.format(30, tree.search(30)))

print("Tree original")
print(tree._traverse(tree.root))

print('Delete {}: {}'.format(30, tree.delete(30)))

print(tree.search(30)) 

print("Tree original")
print(tree._traverse(tree.root))

print('Min: {}'.format(tree.min().data)) 


print('Max: {}'.format(tree.max().data))


