# idea here is to use a second stack to keep track of the minimum value
# stack = [-2, 0, -3]
# minStack = [-2, -2, -3]
# so then if you pop from the stack, also pop the minstack
# this works as oppose to simply keeping track the min value
# as it will break as soon as you pop the minimum value from the stack
# (no way of keeping track if the value is really the mininum, well you can
# keep track of it by comparing it every time, but it'll be O(n))

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack == []:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.minStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        
