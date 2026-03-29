class MyQueue:
    def __init__(self):
        self.stack_one = []
        self.stack_two = []

    def push(self, x: int) -> None:
        while(len(self.stack_two)):
            number = self.stack_two.pop()
            self.stack_one.append(number)

        self.stack_one.append(x)

        while(len(self.stack_one)):
            number = self.stack_one.pop()
            self.stack_two.append(number)

    def pop(self) -> int:
        return self.stack_two.pop()

    def peek(self) -> int:
        return self.stack_two[-1]

    def empty(self) -> bool:
        return len(self.stack_two) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()