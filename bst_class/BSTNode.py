class BSTNode:

    def __init__(self, left, right, parent, value, key):
        self.left = left
        self.right = right
        self.parent = parent
        self.value = value
        self.key = key

    def hasLeftChild(self):
        return self.left
    
    def hasLeftChild(self):
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

    
    



    