from node import Node

class LinkedList:
    def __init__(self):
        self.firstValue = None

    def print(self):
        item = self.firstValue
        while item is not None:
            print(item.item)
            item = item.next



l = LinkedList()
l.firstValue = Node("Sunday")
e2 = Node("Monday")
e3 = Node("Tuesday")
l.firstValue.next = e2
e2.next = e3

l.print()
