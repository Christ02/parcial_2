class Node:
    def __init__(self, data: int):
        self.data = data
        self.left_child = None
        self.right_child = None
        
    def __repr__(self):
        return '({})'.format(self.data)

class AVL_Tree:
    
    def __init__(self):
        self.root = None
        
    
    def insert(self, value: int):
        
        if self.root is None:
            self.root = Node(value)

        else:
            self._insert(value, self.root)
            
    def _insert(self, value: int, subtree: Node):

        if value < subtree.data:
            if subtree.left_child is None:
                subtree.left_child = Node(value)
            else:
                self._insert(value, subtree.left_child)
        
        elif value > subtree.data:
            if subtree.right_child is None:
                subtree.right_child = Node(value)
            else:
                self._insert(value, subtree.right_child)

        else:
            print('Value already exists in tree...')
        
        
    def search(self, key: int) -> bool:
        
        if self.root is None:
            return False
        
        else:
            return self._search(key, self.root)
        
    def _search(self, key: int, subtree: Node) -> bool:
        
        if key == subtree.data:
            return True
        
        elif (key < subtree.data) and (subtree.left_child is not None):
            return self._search(key, subtree.left_child)
        
        elif (key > subtree.data) and (subtree.right_child is not None):
            return self._search(key, subtree.right_child)

        else:
            return False
        
    def delete(self, data):
        if self.root is None:
            return
        
        self.root = self._delete(self.root, data)
        
    def _delete(self, node, data):
        if node is None:
            return None
        
        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:

            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            min_node = self._min(node.right)
            node.data = min_node.data
            node.right = self._delete(node.right, min_node.data)
            
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        
        balance_factor = self.balance(node)
        
        if balance_factor > 1 and self.balance(node.left) >= 0:
            return self.rotate_right(node)
        
        if balance_factor > 1 and self.balance(node.left) < 0:
            return self.rotate_left_right(node)
        
        if balance_factor < -1 and self.balance(node.right) <= 0:
            return self.rotate_left(node)
        
        if balance_factor < -1 and self.balance(node.right) > 0:
            return self.rotate_right_left(node)
        
        return node
    

    def min(self):
        if self.root is None:
            return None
        
        return self._min(self.root)

    def _min(self, node):
        if node.left is None:
            return node
        
        return self._min(node.left)

    def max(self):
        if self.root is None:
            return None
        
        return self._max(self.root)

    def _max(self, node):
        if node.right is None:
            return node
        
        return self._max(node.right)
    


    