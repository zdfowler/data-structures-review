from node import Node

class LinkedList:
    def __init__(self):
        self.firstValue = None

    def print(self):
        item = self.firstValue
        while item is not None:
            print(item.item)
            item = item.next

    def addToEnd(self,someValue):
        node = Node(someValue)
        if self.firstValue is None:
            self.firstValue = node
            return True
        h = self.firstValue
        while h.next is not None:
            h = h.next
        h.next = node
        return True

    def addToStart(self,someValue):
        node = Node(someValue)
        node.next = self.firstValue
        self.firstValue = node
        return True

    def findNode(self,valueToFind):
        i = self.firstValue
        while i is not None:
            if i.item == valueToFind:
                return i
            i = i.next
        return None

    def addAfter(self,someValue,newNodeValue):
        node = self.findNode(someValue)
        if node is not None:
            newNode = Node(newNodeValue)
            newNode.next = node.next
            node.next = newNode
            return True
        else:
            print("Could not find",someValue)
            return False

    def remove(self,needle):
        i = self.firstValue.next
        p = self.firstValue
        if p.item == needle:
            print("Found match at beginning")
            n = self.firstValue.next
            del self.firstValue
            self.firstValue = n
            return True

        while i is not None:
            if i.item == needle:
                p.next = i.next
                del i
                return True
            p = i
            i = i.next
        return False

l = LinkedList()
l.addToEnd("Sunday")
l.addToEnd("Wednesday")
l.addToStart("Saturday")
l.print()
l.addAfter("Sunday","Monday")
l.addAfter("Monday","Tuesday")
l.print()
print(l.remove("Tuesday"))
print(l.remove("Tuesday"))
print(l.remove("Saturday"))
l.print()
l.addAfter("Tuesday","Thursday")
l.addAfter("Wednesday","Thursday")

l.print()
