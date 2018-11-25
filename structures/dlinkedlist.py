class DNode:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
    def print(self):
        print("Node: ",self)
        print("--Data:",self.data)
        print("--Prev:",self.prev)
        print("--Next:",self.next)

class DoublyLinkedList:
    def __init__(self):
        self.firstNode = None
        self.lastNode = None

    def print(self):
        item = self.firstNode
        print("START")
        while item is not None:
            print(item.data)
            item = item.next
        print("END")
        self.printEnds

    def printReverse(self):
       item = self.lastNode
       print("END")
       while item is not None:
           print(item.data)
           item = item.prev
       print("START")
       self.printEnds()

    def printEnds(self):
        if self.lastNode is not None:
            print("lastNode: ",self.lastNode.data)
            self.lastNode.print()
        else:
            print("lastNode: None")
        if self.firstNode is not None:
            print("firstNode: ",self.firstNode.data)
            self.firstNode.print()
        else:
            print("firstNode: None")

    def addToEnd(self,someValue):
        node = DNode(someValue)
        if self.lastNode is None:
            self.lastNode = node
            self.firstNode = node
            return True
        node.prev = self.lastNode
        node.next = None
        self.lastNode.next = node
        self.lastNode = node
        return True

    def addToStart(self,someValue):
        node = DNode(someValue)
        node.prev = None
        if (self.firstNode is None):
            self.firstNode = node
        node.next = self.firstNode
        self.firstNode.prev = node
        self.firstNode = node
        if (self.lastNode is None):
            self.lastNode = self.firstNode
        return True

    def findNode(self,valueToFind):
        i = self.firstNode
        while i is not None:
            if i.data == valueToFind:
                return i
            i = i.next
        return None

    def addAfter(self,someValue,newNodeValue):
        foundNode = self.findNode(someValue)
        foundNode.print()
        if foundNode is not None:
            newNode = DNode(newNodeValue)
            newNode.prev = foundNode
            newNode.next = foundNode.next
            if foundNode.next is not None:
                foundNode.next.prev = newNode 
            else:
                self.lastNode = newNode
            foundNode.next = newNode
            return True
        else:
            print("Could not find",someValue)
            return False

    def remove(self,needle):
        foundNode = self.findNode(needle)
        if foundNode is None:
            print("Could not find",someValue)
            return False

        if foundNode.next is None:
            foundNode.prev.next = None
            self.lastNode = foundNode.prev

        elif foundNode.prev is None:
            foundNode.next.prev = None
            self.firstNode = foundNode.next

        else:
            foundNode.next.prev = foundNode.prev
            foundNode.prev.next = foundNode.next

        del foundNode
        return True


d = DoublyLinkedList()
d.addToStart("Monday")
d.addToEnd("Tuesday")
d.addToEnd("Wednesday")
d.addToStart("Sunday")
d.print()
print("Showing in reverse")
d.printReverse()
print("Remove Wednesday")
d.remove("Wednesday")
d.print()
d.printReverse()
print("Adding Th to end")
d.addToEnd("Thursday")
d.print()
d.printReverse()
print("Add W after Tu")
d.addAfter("Tuesday","Wednesday")
d.print()
d.printReverse()
