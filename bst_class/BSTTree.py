from BSTNode import Node

class Tree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key, val):
        """Insert key, val pair into tree"""
        curr = self.root
        if not curr:
            self.root = Node(key, val)
        else:
            while(True):
                par = curr
                if key < curr.key:
                    curr = curr.left
                    if not curr:
                        par.left = Node(key=key, value=val, left=None, right=None, parent=par)
                        break
                else:
                    curr = curr.right
                    if not curr:
                        par.right = Node(key=key, value=val, left=None, right=None, parent=par)
                        break
        self.size += 1

    def __setitem__(self, k, v):
        self.put(k, v)

    def sortedOrder(self):
        def inOrderWalk(node):
            if not node:
                return
            inOrderWalk(node.left)
            print(node.key)
            inOrderWalk(node.right)
        return inOrderWalk(self.root)

    def get(self, key):
        if not self.root:
            return None
        curr = self.root
        while(curr):
            if key > curr.key:
                curr = curr.right
            elif key < curr.key:
                curr = curr.left
            else:
                return curr.value
        return None

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self.get(key):
            return True
        else:
            return False
            

    
    
        



    




            
            
            
            

