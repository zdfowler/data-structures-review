from node import Node

class LinkedList:
    def __init__(self):
        self.firstValue = None

    def print(self):
        item = self.firstValue
        while item is not None:
            print(item.item)
            item = item.next

    def addToEnd(self,node):
        if self.firstValue is None:
            self.firstValue = node
            return True
        h = self.firstValue
        while h.next is not None:
            h = h.next
        h.next = node
        return True

    def addToStart(self,node):
        node.next = self.firstValue
        self.firstValue = node
        return True

    def findNode(self,nodeToFind):
        i = self.firstValue
        while i is not None:
            if i.item == nodeToFind.item:
                return i
            i = i.next
        return None

    def addAfter(self,existingNode,newNode):
        node = self.findNode(existingNode)
        if node is not None:
            newNode.next = node.next
            node.next = newNode
        else:
            print("Could not find",existingNode.item)
            return False

    def remove(self,needle):
        i = self.firstValue.next
        p = self.firstValue
        if p.item == needle.item:
            print("Found match at beginning")
            n = self.firstValue.next
            del self.firstValue
            self.firstValue = n
            return True

        while i is not None:
            if i.item == needle.item:
                p.next = i.next
                del i
                return True
            p = i
            i = i.next
        return False

l = LinkedList()
l.firstValue = Node("Sunday")
e2 = Node("Monday")
e3 = Node("Tuesday")
l.firstValue.next = e2
e2.next = e3
l.addToEnd(Node("Wednesday"))
l.addToStart(Node("Saturday"))
l.print()
print(l.remove(Node("Tuesday")))
print(l.remove(Node("Tuesday")))
print(l.remove(Node("Saturday")))
l.print()
l.addAfter(Node("Tuesday"),Node("Thursday"))
l.addAfter(Node("Wednesday"),Node("Thursday"))

l.print()
