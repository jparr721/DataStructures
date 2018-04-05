class Stack:
    def __init__(self):
        self.stack = []

    def empty(self):
        return self.stack == []

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def pop(self):
        return self.stack.pop()

    def push(self, data):
        return self.stack.push(data)

    def search(self, value):
        for i in range(len(self.stack) - 1):
            if value == self.stack[i]
                return i
        return None 


