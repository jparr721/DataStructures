from typing import Any


class ThreeStacks:
    def __init__(self):
        # Stack 1 range 0 - 1, 2 1 - 2, 2 len(stack)
        # Non inclusive
        self.ends = [0, 1, 2]

        self.stack = [None, None, None]

        self.coordinates = {
            1: self.ends[1],
            2: self.ends[2],
            3: len(self.stack),
        }

    def __repr__(self):
        string = ""
        string += f"1: {repr(self.stack[0:self.coordinates[2]])}\n"
        string += f"2: {repr(self.stack[self.coordinates[1]:self.coordinates[2]])}\n"
        string += f"3: {repr(self.stack[self.coordinates[2]:self.coordinates[3]])}"

        return string

    def push(self, value: Any, stack_number: int) -> None:
        print(self.ends)
        stack_address = self.check_pos(stack_number)

        if stack_number == 3:
            if not self._check_insert(stack_number):
                self.stack.append(value)
            else:
                self.stack[stack_number - 1] = value
        else:
            if not self._check_insert(stack_number):
                self.stack.append(None)

                for i in range(stack_address, len(self.stack) - 1):
                    self.stack[i + 1] = self.stack[i]
                self.stack[stack_address] = value
            else:
                self.stack[stack_number - 1] = value

        self.ends[stack_number - 1] += 1

    def _check_insert(self, stack_number):
        if not self.stack[stack_number - 1]:
            return True
        return False

    def check_pos(self, stack_number: int) -> int:
        print(stack_number)
        print('+'*40)
        print(self.coordinates[stack_number])
        print('+'*40)
        if stack_number > 3 or stack_number < 0:
            raise ValueError("Invalid stack number")

        return self.coordinates[stack_number]


if __name__ == "__main__":
    ts = ThreeStacks()
    ts.push(1, 1)
    print(ts)
    print("==")
    ts.push(1, 1)
    ts.push(1, 1)
    print(ts)
    print("==")
    ts.push(1, 2)
    print(ts)
    print("==")
    ts.push(1, 2)
    print(ts)
    print("==")
    ts.push(1, 3)
    print(ts)
    print("==")
    ts.push(1, 3)
    print(ts)
    print("==")
    ts.push(1, 3)
    print(ts)
