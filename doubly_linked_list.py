#! /usr/local/bin/python
''' tested with Python 3.7.0 '''

'''
Doubly linked list operations.
'''

# Double Linked List Node
class Node:
    def __init__(self, data):
        '''constructor'''
        self.data = data
        self.next = None
        self.prev = None

# Double Linked List class
class DoublyLinkedList:

    def __init__(self):
        '''constructor'''
        self.__head = None
        self.__tail = None

    def printData(self):
        '''Prints all the data in the list'''
        iter = self.__head
        while iter is not None:
            print(iter.data)
            iter = iter.next

    def printDataReverse(self):
        '''Prints all the data in the list'''
        iter = self.__tail
        while iter is not None:
            print(iter.data)
            iter = iter.prev

    def addHeadNode(self, data):
        '''Adds a new node at the head'''
        node = Node(data)
        if self.__head is None and self.__tail is None:
            self.__head = self.__tail = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    def addTailNode(self, data):
        '''Adds a new node at the tail'''
        node = Node(data)
        if self.__head is None and self.__tail is None:
            self.__head = self.__tail = node
        else:
            node.prev = self.__tail
            self.__tail.next = node
            self.__tail = node

    def deleteHeadNode(self):
        '''Deletes a node at the Head'''
        data = None
        if self.__head is not None:
            data = self.__head.data
            self.__head = self.__head.next
            self.__head.prev = None

        return data

    def deleteTailNode(self):
        '''Deletes a node at the Tail'''
        data = None
        if self.__tail is not None:
            data = self.__tail.data
            self.__tail = self.__tail.prev
            self.__tail.next = None

        return data

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
                    self.__tail = iter.prev

                # Check if this is not a Head Node.
                if iter.prev is not None:
                    iter.prev.next = iter.next
                else:
                    self.__head = iter.next

                # Should all notes be deleted or no?
                if all == False:
                    break

            iter = iter.next

    def traverse(self):
        '''Prints all the link information in the list'''
        iter = self.__head
        count = 1
        while iter is not None:
            print(f"{count}, prev: {iter.prev}, self: {iter}, next: {iter.next}, data: {iter.data}")
            iter = iter.next
            count += 1

if __name__ == "__main__":
    d = DoublyLinkedList()

    # Add new nodes at the tail with some duplicate data
    d.addTailNode(5)
    d.addTailNode(6)
    d.addTailNode(7)
    d.addTailNode(8)
    d.addTailNode(9)
    d.addTailNode(9)
    d.addTailNode(9)
    d.addTailNode(9)
    d.addTailNode(10)
    d.printData()
    print("added new nodes to Tail")

    d.addHeadNode(4)
    d.printData()
    print("added new data at head")

    print(d.deleteHeadNode())
    d.printData()
    print("Deleted Head node")

    print(d.deleteTailNode())
    d.printData()
    print("Deleted tail node")

    d.deleteNode(9)
    d.printData()
    print("Deleted one node with some data")

    d.deleteNode(9, all=True)
    d.printData()
    print("Deleted all nodes with same data")

    d.traverse()
    print("traverse through all the links")

    d.printDataReverse()
    print("print data in reverse\n")


