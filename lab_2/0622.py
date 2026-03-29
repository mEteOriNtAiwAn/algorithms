class MyCircularQueue:
    def __init__(self, k: int):
        self.stack_one = []
        self.stack_two = []
        self.max_size = k

    def distillation(self, a, b):
        while(len(a)):
            number = a.pop()
            b.append(number)

        return b

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False

        self.stack_one = self.distillation(self.stack_two, self.stack_one)
        self.stack_one.append(value)
        self.stack_two = self.distillation(self.stack_one, self.stack_two)
        
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False

        self.stack_two.pop()
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.stack_two[-1]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.stack_two[0]

    def isEmpty(self) -> bool:
        return len(self.stack_two) == 0

    def isFull(self) -> bool:
        return len(self.stack_two) == self.max_size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()