# Implement three stacks with a single array
# Could implement first/second/third helper function
import math
from collections import deque


class ThreeStacks:
    def __init__(self, array_constructor):
        self.array_constructor = array_constructor
        if len(array_constructor) % 3 == 0:
            self.first = deque(array_constructor[0:int(len(array_constructor)/3)])
            self.second = deque(array_constructor[int(len(array_constructor) / 3):int(len(array_constructor) * 2 / 3)])
            self.third = deque(array_constructor[int(len(array_constructor) * 2 / 3):])
        else:
            self.first = deque(self.array_constructor[0:math.floor(len(array_constructor)/3)])
            self.second = deque(self.array_constructor[
                                math.floor(len(array_constructor)/3):math.floor(len(array_constructor)*2/3)])
            self.third = deque(self.array_constructor[math.floor(len(array_constructor)*2/3):])

    def is_empty_stack(self):
        if len(self.array_constructor) == 0:
            return True

    def push_stack(self, element):
        self.array_constructor.append(element)
        array_constructor = [x for x in self.array_constructor]
        if len(array_constructor) % 3 == 0:
            self.first = deque(array_constructor[0:int(len(array_constructor)/3)])
            self.second = deque(array_constructor[int(len(array_constructor)/3):int(len(array_constructor) * 2/3)])
            self.third = deque(array_constructor[int(len(array_constructor) * 2/3):])
        else:
            self.first = deque(array_constructor[0:math.floor(len(array_constructor)/3)])
            self.second = \
                deque(array_constructor[math.floor(len(array_constructor)/3):math.floor(len(array_constructor)*2/3)])
            self.third = deque(array_constructor[math.floor(len(array_constructor)*2/3):])
        return ThreeStacks(array_constructor)

    def pop_stack(self):
        if len(self.array_constructor) == 0:
            raise Exception("stack is empty")
        self.array_constructor.pop()
        array_constructor = [x for x in self.array_constructor]
        if len(array_constructor) % 3 == 0:
            self.first = deque(array_constructor[0:int(len(array_constructor) / 3)])
            self.second = deque(array_constructor[int(len(array_constructor) / 3):int(len(array_constructor) * 2 / 3)])
            self.third = deque(array_constructor[int(len(array_constructor) * 2 / 3):])
        else:
            self.first = deque(array_constructor[0:math.floor(len(array_constructor) / 3)])
            self.second = \
                deque(array_constructor[
                      math.floor(len(array_constructor) / 3):math.floor(len(array_constructor) * 2 / 3)])
            self.third = deque(array_constructor[math.floor(len(array_constructor) * 2 / 3):])
        return ThreeStacks(array_constructor)

    def peek_stack(self):
        return print(self.array_constructor[len(self.array_constructor) - 1])


if __name__ == "__main__":
    array_stack = ["a,", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
    check = ThreeStacks(array_stack)
    print(check.first)
    print(check.second)
    print(check.third)
    check.push_stack("l")
    print(check.first)
    print(check.second)
    print(check.third)
    check.push_stack("m")
    check.peek_stack()
    print(check.first)
    print(check.second)
    print(check.third)
    check.push_stack("n")
    check.push_stack("o")
    check.peek_stack()
    print(check.first)
    print(check.second)
    print(check.third)
    print(check.first)
    check.pop_stack()
    check.pop_stack()
    print(check.first)
    print(check.second)
    print(check.third)
    array_empty = []
    check2 = ThreeStacks(array_empty)
    print(check2.is_empty_stack())
