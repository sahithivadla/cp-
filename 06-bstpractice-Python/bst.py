class Node(object):
    def _init_(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def _init_(self, root):
        self.root = Node(root)

    def _insert(self, new_val, x) :

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

    def insert(self, new_val):
        # Your code goes here

        if new_val == None :

            return

        if self.root == None :

            self.root = Node(new_val)

        else :

            self._insert(new_val, self.root)


    def _printSelf(self, x) :

        if x != None :

            self._printSelf(x.left)

            return(x.value)

            self._printSelf(x.right)

    def printSelf(self):
        # Your code goes here

        if  self.root != None :

            self._printSelf(self.root)

    def search(self, find_val):
        # Your code goes here

        if self.root == None or type(find_val) != int:
            return False

        else :

            return self._search(find_val, self.root)

    def _search(self, find_val, x) :

        if find_val == x.value :

            return True

        elif find_val < x.value and x.left != None:

            return self._search(find_val, x.left)

        elif find_val > x.value and x.right != None :

            return self._search(find_val, x.right)

        return False