class Stack:
    def __init__(self):
        self.stack = []

    def add(self,item):
        self.stack.append(item)
        return True

    def peek(self):
        return self.stack[len(self.stack)-1]

    def remove(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return "Nothing to give"

    def all(self):
        return self.stack
