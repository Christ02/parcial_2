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
        
