#! /usr/local/bin/python
''' tested with Python 3.7.0 '''

class Node:
    def __init__(self, data):
        self.data  = data
        self.left  = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def min(self):
        iter = self.root
        while iter.left:
            iter = iter.left
        return iter.data

    def max(self):
        iter = self.root
        while iter.right:
            iter = iter.right
        return iter.data

    def insert(self, data):
        '''insert a new node into the tree.'''
        if self.root is None:
            self.root = Node(data)
            self.left = None
            self.right = None
            return

        def insertNode(node, data):
            if data < node.data:
                if node.left is None:
                    node.left = Node(data)
                else:
                    insertNode(node.left, data)
            else:
                if node.right is None:
                    node.right = Node(data)
                else:
                    insertNode(node.right, data)

        insertNode(self.root, data)

    def inorderTraversal(self, data):
        '''insert a new node into the tree.'''
        if self.root is None:
            self.root = Node(data)
            self.left = None
            self.right = None
            return

        def insertNode(node, data):
            if data < node.data:
                if node.left is None:
                    node.left = Node(data)
                else:
                    insertNode(node.left, data)
            else:
                if node.right is None:
                    node.right = Node(data)
                else:
                    insertNode(node.right, data)

        insertNode(self.root, data)

    # def delete(self, data):



    def is_mirror(t1, t2):
        if t1 is None and t2 is None:
            return True
        else:
            return t1 is not None and \
                t2 is not None and \
                t1.data == t2.data and \
                is_mirror(t1.left, t2.right) and \
                is_mirror(t1.right, t2.left)