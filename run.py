from search.binary import binSearch
from structures.stack import Stack
from array import *
from structures.linkedlist import LinkedList

a = [1,3,6,8]
found = binSearch(a,3)
if found != -1:
    print("Found it at ",found)
else:
    print("Didn't find it. :( ")


s = Stack()
s.add(7)
s.add(2)
s.add(3)
s.add(7)
s.add(7)
print(s.all())
print(s.peek())
print("popped",s.remove())
print(s.peek())
print("popped",s.remove())
s.add(99)
print("peek",s.peek())
print("all",s.all())
print(s)
print(s.remove())
print(s.remove())
print(s.remove())
print(s.remove())
print(s.remove())
print(s.remove())

ar = array("i",[3,4,5,7,8,12,1,4,2,])

print (ar[1])
print("------------------Linked list-------------------")

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
