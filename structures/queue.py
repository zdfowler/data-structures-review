class Queue:
    def __init__(self):
        self.queue = [] #list

    def add(self,item):
        self.queue.insert(0,item)

    def size(self):
        return len(self.queue)

    def remove(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        else:
            return False
    def print(self):
        for i in self.queue:
            print(i)

q = Queue()
q.add("Monday")
q.add("Tuesday")
q.add("Wednesday")
q.print()
print("Popping ", q.remove())
q.print()
q.add("Thursday")
q.print()
