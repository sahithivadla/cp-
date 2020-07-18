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
        if(self.root == None or find_val == self.root):
            return self.root
        if self.root.value < find_val:
            return search(root.right,key)




    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        # Your code goes here
        return self.value

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        # Your code goes here
        pass

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        # Your code goes here
        pass
