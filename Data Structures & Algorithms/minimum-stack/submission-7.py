class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0 and len(self.minStack) == 0:
            self.minStack.append(val)
            self.stack.append(val)
            return

        self.stack.append(val)

        if self.minStack and val < self.minStack[-1] :
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

        print(self.minStack, self.stack)


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]