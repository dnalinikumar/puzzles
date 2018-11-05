#! /usr/local/bin/python
''' tested with Python 3.7.0 '''

'''
Given a list of numbers, find top k maximum values.
Return the input list if the list has smaller number of elements.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, node):
        node.next = self.head
        self.head = node

    def deleteNode(self, node):
        self.head = node.next
        return node

    def findLoop(self):
        if self.head != None:
            iter1 = self.head
            iter2 = self.head

            while iter2 != None or iter1 != None:
                iter1 = iter1.next
                iter2 = iter2.next

                if iter2.next is not None:
                    iter2 = iter2.next

                if iter1 == iter2:
                    return True

        return False

