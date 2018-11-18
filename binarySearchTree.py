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
        while iter and iter.left:
            iter = iter.left
        return iter and iter.data

    def max(self):
        iter = self.root
        while iter and iter.right:
            iter = iter.right
        return iter and iter.data

    def insert(self, data):
        '''insert a new node into the tree.'''
        if self.root is None:
            self.root = Node(data)
            self.size = 1
            return True

        def insertNode(node, data):
            if data < node.data:
                if node.left is None:
                    node.left = Node(data)
                else:
                    return insertNode(node.left, data)
            elif data > node.data:
                if node.right is None:
                    node.right = Node(data)
                else:
                    return insertNode(node.right, data)
            else:
                raise ValueError

        try:
            insertNode(self.root, data)
        except ValueError:
            return False
        else:
            self.size += 1
            return True


    def delete(self, data):
        '''delete a node from the tree.'''
        if self.root is None:                   # no nodes in the tree
            return False
        elif self.root.data == data:            # root node to be deleted
            if self.root.left is None:          # root node to be deleted with no left node.
                self.root = self.root.right
            elif self.root.right is None:       # root node to be deleted with no right node.
                self.root = self.root.left
            else:                               # root node to be deleted, but left and right nodes present.
                prev = iter = self.root.left
                while iter and iter.right:      # go till the right most node on the left sub tree.
                    prev = iter
                    iter = iter.right

                if iter != self.root.left:      # If right nodes are present on the left subtree
                    prev.right = iter.left

                iter.right = self.root.right
                self.root = iter

            self.size -= 1
            return True
        else:                                   # non root node to be found, deleted
            prev = iter = self.root
            while iter:
                if data < iter.data:            # go to the left subtree
                    prev = iter
                    iter = iter.left
                elif data > iter.data:          # go to the right subtree
                    prev = iter
                    iter = iter.right
                else:                           # node found.
                    break

            if iter is None:                    # Node with the data not found.
                return False

            if iter.left is None:               # No left subtree from the node found.
                if prev.left == iter:
                    prev.left = iter.right
                elif prev.right == iter:
                    prev.right = iter.right
            elif iter.right is None:            # No right subtree from the node found.
                if prev.left == iter:
                    prev.left = iter.left
                elif prev.right == iter:
                    prev.right = iter.left
            else:                               # have both left and right children
                if prev.left == iter:           # left side of its parent
                    prev1 = iter = iter.right
                    while iter.left:
                        prev1 = iter
                        iter = iter.left

                    if prev1 == iter:           # no further left subtree
                        prev1.left = prev.left.left
                        prev.left = prev1
                    else:
                        prev1.left = iter.right
                        iter.right = prev.left.right
                        iter.left = prev.left.left
                        prev.left = iter

                elif prev.right == iter:        # right side of its parent
                    prev1 = iter = iter.left
                    while iter.right:
                        prev1 = iter
                        iter = iter.right

                    if prev1 == iter:            # no further right subtree
                        prev1.right = prev.right.right
                        prev.right = prev1
                    else:
                        prev1.left = iter.right
                        iter.right = prev.right.right
                        iter.left = prev.right.left
                        prev.right = iter
                        
            self.size -= 1
            return True

    def inorderTraversal(self):
        '''In order traversal.'''
        def inorder(node):
            if node is not None:
                inorder(node.left)
                print(' ', node.data, end='')
                inorder(node.right)

        inorder(self.root)

    def preorderTraversal(self):
        '''pre order traversal.'''
        def preorder(node):
            if node is not None:
                print(' ', node.data, end='')
                preorder(node.left)
                preorder(node.right)

        preorder(self.root)

    def postorderTraversal(self):
        '''post order traversal.'''
        def postorder(node):
            if node is not None:
                postorder(node.right)
                postorder(node.left)
                print(' ', node.data, end='')

        postorder(self.root)


def is_mirror(t1, t2):
    '''check if two binary trees are mirror image to each other.'''
    if t1 is None and t2 is None:
        return True
    else:
        return t1 and t2 and \
            t1.data == t2.data and \
            is_mirror(t1.left, t2.right) and \
            is_mirror(t1.right, t2.left)

if __name__ == '__main__':
    # Create a binary search tree
    t = BinarySearchTree()

    # Insert elements
    t.insert(3)
    t.insert(5)
    t.insert(7)
    t.insert(2)
    t.insert(9)
    t.insert(0)
    t.insert(-3)
    t.insert(1)
    t.insert(200)
    t.insert(-9)

    # inorder traversal
    print('\nInorder traversal:')
    t.inorderTraversal()

    # preorder traversal
    print('\nPreorder traversal:')
    t.preorderTraversal()

    # postorder traversal
    print('\nPostorder traversal:')
    t.postorderTraversal()

    print('\n')

    # delete an element.
    t.delete(2)

    # inorder traversal
    print('\nInorder traversal:')
    t.inorderTraversal()

    # preorder traversal
    print('\nPreorder traversal:')
    t.preorderTraversal()

    # postorder traversal
    print('\nPostorder traversal:')
    t.postorderTraversal()
    print('\n')
