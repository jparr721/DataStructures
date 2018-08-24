class Stack(object):
    def __init__(self):
        self._min = 100000000000
        self.stack = []
        self.historic_mins = []

    def push(self, item):
        if item not in self.stack:
            self.stack.append(item)
            if item < self._min:
                self.historic_mins.append(item)
                self._min = item

    def pop(self):
        old_min = self.stack.pop()
        if self._min == old_min:
            self.historic_mins.pop()
            self._min = self.historic_mins[0]

    @property
    def min(self):
        return self._min

    @property
    def print_stack(self):
        print(self.stack)


stack = Stack()
stack.push(1)
stack.push(2)
print(stack.historic_mins)
stack.push(3)
print(stack.min)
stack.print_stack
stack.push(-5)
stack.push(6)
print(stack.historic_mins)
print(stack.min)
stack.print_stack
stack.pop()
stack.pop()
print(stack.historic_mins)
print(stack.min)
stack.print_stack
