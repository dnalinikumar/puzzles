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
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        '''constructor'''
        self.__head = None
        self.__tail = None

    def addHeadNode(self, node):
        '''Adds a new node at the head'''
        if self.__head is None and self.__tail is None:
            self.__head = self.__tail = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    def addTailNode(self, node):
        '''Adds a new node at the tail'''
        if self.__head is None and self.__tail is None:
            self.__head = self.__tail = node
        else:
            node.prev = self.__tail
            self.__tail.next = node
            self.__tail = node

    def deleteHeadNode(self, node):
        '''Deletes a node at the Head'''
        if self.__head is not None:
            self.__head = self.__head.next
            self.__head.prev = None

    def deleteTailNode(self, node):
        '''Deletes a node at the Tail'''
        if self.__tail is not None:
            self.__tail = self.__tail.prev
            self.__tail.next = None

    def deleteNode(self, data, all=False):
        '''
        Deletes a node(s) based on the data.
        if all=True, then all the nodes matching the data would be deleted.
        '''
        iter = self.__head
        while iter is not None:
            if iter.data == data:
                if iter.next is not None:
                    iter.next.prev = iter.prev
                else:
                    iter.next.prev = None
                    self.__tail = iter.prev

                # Check if this is not a Head Node.
                if iter.prev is not None:
                    iter.prev.next = iter.next
                else:
                    iter.next.prev = None
                    self.__head = iter.next

                # Should all notes be deleted or no?
                if all == False:
                    break


