#! /usr/local/bin/python
''' tested with Python 3.7.0 '''

'''
Singly linked list operations.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        '''constructor'''
        self.__head = None

    def printData(self):
        '''Prints all the data in the list'''
        iter = self.__head
        while iter is not None:
            print(iter.data)
            iter = iter.next

    def printDataReverse(self):
        '''Prints all the data in the list'''
        def getData(iter):
            if iter is not None:
                getData(iter.next)
                print(iter.data)

        getData(self.__head)

    def addNode(self, data):
        '''Adds a new node at the head'''
        node = Node(data)
        if self.__head is None:
            self.__head = node
        else:
            node.next = self.__head
            self.__head = node

    def deleteHeadNode(self):
        '''Deletes a node at the Head'''
        data = None
        if self.__head is not None:
            data = self.__head.data
            self.__head = self.__head.next

        return data

    def deleteNode(self, data, all=False):
        '''
        Deletes a node(s) based on the data.
        if all=True, then all the nodes matching the data would be deleted.
        '''
        prev = iter = self.__head
        while iter is not None:
            if iter.data == data:
                if iter == self.__head:
                    self.__head = iter.next
                else:
                    prev.next = iter.next

                # Should all notes be deleted or no?
                if all == False:
                    break

            prev = iter
            iter = iter.next

    def traverse(self):
        '''Prints all the link information in the list'''
        iter = self.__head
        count = 1
        while iter is not None:
            print(f"{count}, self: {iter}, next: {iter.next}, data: {iter.data}")
            iter = iter.next
            count += 1

    def getNumberFromNodes(self):
        ''' get the number from linked list nodes'''
        iter = self.__head
        data = 0

        while iter is not None:
            data = data * 10 + iter.data
            iter = iter.next

        return data



if __name__ == '__main__':
    d = SinglyLinkedList()

    # Add new nodes at the tail with some duplicate data
    d.addNode(5)
    d.addNode(6)
    d.addNode(7)
    d.addNode(8)
    d.addNode(9)
    d.addNode(9)
    d.addNode(9)
    d.addNode(9)
    d.addNode(10)
    d.printData()
    print("added new nodes")

    print(d.deleteHeadNode())
    d.printData()
    print("Deleted Head node")

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

    #------------- add two numbers in two linked lists ------

    x = SinglyLinkedList()
    y = SinglyLinkedList()

    x.addNode(5)
    x.addNode(6)
    x.addNode(2)
    x.addNode(1)
    xNum = x.getNumberFromNodes()

    y.addNode(9)
    y.addNode(8)
    y.addNode(7)
    yNum = y.getNumberFromNodes()

    print(xNum + yNum)


