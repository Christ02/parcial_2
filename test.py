from AVL_tree import AVL_Tree


tree = AVL_Tree()

tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)

# Search for value
print(tree.search(30)) # True


tree.delete(30)

print(tree.search(30)) # False

print(tree.min().data) # 10

print(tree.max().data) # 50
