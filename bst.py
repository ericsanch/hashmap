class Word:
    def __init__(self, number, key):
        self.count = number  # this will serve as the object's key
        self.key = key

    def __lt__(self, kq):
        if kq > self.count:
            return True

    def __gt__(self, kq):
        if kq < self.count:
            return True

    def __eq__(self, kq):
        if kq == self.count:
            return True

    def __str__(self):
        if self.count is not None:
            out = self.key + " " + str(self.count)
            return out


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class BST:
    def __init__(self, start_tree=None) -> None:
        """ Initialize empty tree """
        self.root = None

        # populate tree with initial nodes (if provided)
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self):
        """
        Traverses the tree using "in-order" traversal
        and returns content of tree nodes as a text string
        """
        values = [str(_) for _ in self.in_order_traversal()]
        return "TREE in order { " + ", ".join(values) + " }"

    def add(self, val):
        """
        Creates and adds a new node to the BSTree.
        If the BSTree is empty, the new node should added as the root.

        Args:
            val: Item to be stored in the new node
        """
        new_node = TreeNode(val)
        cur = self.root
        # create root node if BST is empty
        if self.root is None:
            self.root = new_node
        # find location for new leaf and insert
        else:
            cur = self.depth_first_traversal(val)
            if cur.val > val:
                cur.left = new_node
            else:
                cur.right = new_node

    # helper function for finding the in-order location for a new leaf
    def depth_first_traversal(self, val):
        cur = self.root
        while True:
            if cur.val > val:
                if cur.left is None:
                    return cur
                cur = cur.left
            else:
                if cur.right is None:
                    return cur
                cur = cur.right

    def contains(self, kq):
        """
        Searches BSTree to determine if the query key (kq) is in the BSTree.

        Args:
            kq: query key
        Returns:
            True if kq is in the tree, otherwise Fals
        """
        cur = self.root
        while cur != None:
            if kq > cur.val:
                cur = cur.right
            elif kq < cur.val:
                cur = cur.left
            elif kq == cur.val:
                return True
        return False

    def left_child(self, node):
        """
        Returns the left-most child in a subtree.

        Args:
            node: the root node of the subtree

        Returns:
            The left-most node of the given subtree
        """
        cur = node
        while cur.left is not None:
            node = cur
            cur = cur.left
        return cur
    # helper function to get greatest value in tree
    def getRight(self):
        cur = self.root
        while cur.right is not None:
            cur = cur.right
        return cur

    # helper function to determine if a node is a leaf
    def no_child(self, node):
        if node.left is None and node.right is None:
            return True
        else:
            return False

    # helper function to determine if a node has only 1 child
    def one_child(self, node):
        if node.left is None and node.right is not None or node.left is not None and node.right is None:
            return True
        else:
            return False

    def remove(self, kq):
        """
        Removes node with key k, if the node exists in the BSTree.

        Args:
            node: root of Binary Search Tree
            kq: key of node to remove

        Returns:
            True if k is in the tree and successfully removed, otherwise False
        """
        # check if removing the root and call remove_first
        if kq == self.root.val:
            return self.remove_first()

        else:
            cur = self.root
            parent = self.root
            # check that tree has node to be removed, return false if not
            if self.contains(kq):
                # find node to be removed its parent
                while cur.val != kq:
                    if kq < cur.val:
                        parent = cur
                        cur = cur.left
                    else:
                        parent = cur
                        cur = cur.right
                # check if node is a leaf
                if self.no_child(cur):
                    if parent.left == cur:
                        parent.left = None
                        return True
                    else:
                        parent.right = None
                        return True

                # check if node has one child
                if self.one_child(cur):
                    if parent.left == cur:
                        if cur.left is None:
                            parent.left = cur.right
                            return True
                        else:
                            parent.left = cur.left
                            return True
                    else:
                        if cur.left is None:
                            parent.right = cur.right
                            return True
                        else:
                            parent.right = cur.left
                            return True

                # if this point is reached, node has 2 children
                # parent and cur set above
                else:
                    successor = self.left_child(cur.right)
                    PS = cur.right
                    if successor == PS:
                        parent.right = successor
                        successor.left = cur.left
                    else:
                        while PS.left is not successor:
                            PS = PS.left
                        # parent.right = successor
                        if parent.left == cur:
                            parent.left = successor
                            # print(successor.val)
                        else:
                            # print(successor.val)
                            parent.right = successor
                        successor.left = cur.left
                        PS.left = successor.right
                        successor.right = cur.right
                        # successor.left = cur.left
                        # temp = cur.left
                        # successor.left = temp
                        # successor.right = cur.right

                    return True
            else:
                # if the function reaches this point, the node to remove was not found
                # and it returns false
                return False


    def get_first(self):
        """
        Gets the val of the root node in the BSTree.

        Returns:
            val of the root node, return None if BSTree is empty
        """
        if self.root is None:
            return None
        else:
            return self.root.val

    def remove_first(self):
        """
        Removes the val of the root node in the BSTree.

        Returns:
            True if the root was removed, otherwise False
        """
        # check if tree contains anything
        if self.root is None:
            return False
        # check if root has more than one child and perform remove
        elif self.root.right is None:
            self.root = self.root.left
            return True
        # if root has one child on right, find successor to move to root and perform remove
        elif self.root.left is None:
            PS = self.root.right
            successor = self.left_child(PS)

            # find how many children PS has, perform remove as necessary
            if self.no_child(PS):
                successor.right = None
                self.root = successor
                return True
            elif self.one_child(PS):
                if PS.left is None:
                    successor.right = PS.right
                else:
                    while PS.left is not successor:
                        PS = PS.left
                    PS.left = None
                    successor.right = self.root.right
                self.root = successor
                return True
            # when PS of a 1 child node has 2 children
            else:
                while PS.left is not successor:
                    PS = PS.left
                PS.left = None
                successor.right = self.root.right
                self.root = successor
                return True

        # in this case root has 2 children
        else:
            PS = self.root.right
            successor = self.left_child(PS)
            if successor is PS:
                PS.left = self.root.left
                self.root = successor
                return True
            else:
                successor.left = self.root.left
                while PS.left is not successor:
                    PS = PS.left
                PS.left = successor.right
                if self.root.right is successor:
                    successor.right = successor.right.right
                else:
                    successor.right = self.root.right
                self.root = successor
                return True