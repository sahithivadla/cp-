class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        # Your code goes here
        if self.root == None or type(find_val) != int :
            return False
        else :
            return self.preorder_search(self.root, find_val)


    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        # Your code goes here
        if self.root == None :
            return
        else :
            self.preorder_print(self.root)

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        # Your code goes here
        if find_val == start.value :
            return True
        elif find_val < start.value and start.left != None :
            return self.preorder_search(start.left, find_val)
        elif find_val > start.value and start.right != None :
            return self.preorder_search(start.right, find_val)
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        # Your code goes here
        self.preorder_print(start.left)
        self.preorder_print(start.right)
