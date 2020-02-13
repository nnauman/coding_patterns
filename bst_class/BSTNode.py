class Node:

    def __init__(self, key, value, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.value = value
        self.key = key

    def __repr__(self):
        return 'Node(%s, %s)' % (self.key, self.value)

    def hasLeftChild(self):
        return self.left
    
    def hasRightChild(self):
        return self.right

    def isRightChild(self):
        return self.parent and self.parent.right == self

    def isLeftChild(self):
        return self.parent and self.parent.left

    def isRoot(self):
        return not self.parent
    
    def isLeaf(self):
        return not self.left and not self.right

    def hasAnyChildren(self):
        return self.left or self.right

    def hasBothChildren(self):
        return self.left and self.right

    def replaceNodeData(self, key, value, left, right):
        # TODO: Implement this
        pass

    def findMin(self):
        curr = self
        while curr.left:
            curr = curr.left
        return curr

    def findMax(self):
        curr = self
        while curr.right:
            curr = curr.right
        return curr

    def findSucessor(self):
        curr = self
        if curr.right:
            curr = curr.right
            while curr.left:
                curr = curr.left
            return curr
        else:
            p = curr.parent
            while p and p.right == curr:
                curr = p
                p = p.parent
            return p
    
        


    

    
    



    