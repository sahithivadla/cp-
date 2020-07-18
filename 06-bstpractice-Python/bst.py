class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Your code goes here
        if new_val < x.value :

            if x.left == None :

                x.left = Node(new_val)

            else :

                self._insert(new_val, x.left)
        else :

            if x.right == None :

                x.right = Node(new_val)

            else :

                self._insert(new_val, self.right)
        pass

    def printSelf(self):
        # Your code goes here
        pass

    def search(self, find_val):
        # Your code goes here
        pass

