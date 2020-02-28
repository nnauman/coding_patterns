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
        while(curr and key != curr.key):
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self.get(key):
            return True
        else:
            return False

    def transplant(self, u, v):
        """Replace the subtree rooted a u with the subtree rooted at v"""
        if not u.parent:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent


    def delete(self, z):
        """Deleted the node z from the BST"""

        if not z.left:
            self.transplant(z, z.right)
        elif not z.right:
            self.transplant(z, z.right)
        else:
            y = z.findMin(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y







    
    
        



    




            
            
            
            

