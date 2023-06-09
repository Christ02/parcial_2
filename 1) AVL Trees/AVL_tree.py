class Node:
    def __init__(self, data): 
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def __repr__(self):
         return '({})'.format(self.data)

class AVL_tree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        
        self.root = self._insert(self.root, data)
        
    def _insert(self, node, data):
        if node is None:
            return Node(data)
        
        if data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)
        
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        balance_factor = self.balance(node)
        
        if balance_factor > 1 and data < node.left.data:
            return self.rotate_right(node)
        
        if balance_factor < -1 and data > node.right.data:
            return self.rotate_left(node)
        
        if balance_factor > 1 and data > node.left.data:
            return self.rotate_left_right(node)
        
        if balance_factor < -1 and data < node.right.data:
            return self.rotate_right_left(node)
        
        return node
    
    def _traverse(self, node):
        if node is None:
            return []
        
        return self._traverse(node.left) + [node.data] + self._traverse(node.right)

    def search(self, data):
        if self.root is None:
            return None
        
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None:
            return None
        
        if data == node.data:
            return node
        
        if data < node.data:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)

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

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        right_child.height = max(self.height(right_child.left), self.height(right_child.right)) + 1
        
        return right_child
    
    def rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        left_child.height = max(self.height(left_child.left), self.height(left_child.right)) + 1
        
        return left_child
    
    def rotate_left_right(self, node):
        node.left = self.rotate_left(node.left)
        return self.rotate_right(node)
    
    def rotate_right_left(self, node):
        node.right = self.rotate_right(node.right)
        return self.rotate_left(node)

    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right) 
