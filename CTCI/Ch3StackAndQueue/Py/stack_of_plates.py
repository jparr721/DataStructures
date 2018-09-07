class SetOfStacks(object):
    def __init__(self, size=5):
        self.size = size
        self._set_of_stacks = [[]]
        self.current_stack = 0

    def push(self, data):
        if len(self._set_of_stacks[self.current_stack]) < self.size:
            current = self._set_of_stacks[self.current_stack]
            current.push(data)
        else:
            new_stack = [data]
            self._set_of_stacks.push(new_stack)
            self.current_stack += 1

    def pop(self):
        current = self._set_of_stacks[self.current_stack]
        data = current.pop()

        if len(current) == 0 and self.current_stack != 0:
            del self._set_of_stacks[self.current_stack]
            self.current_stack -= 1

        return data

    def pop_at(self, index):
        current = self._set_of_stacks[index]
        return current.pop()
