# from collections import deque


class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [-1] * self.k
        self.head = self.tail = 0

    def enQueue(self, value: int) -> bool:
        if self.isEmpty():
            self.queue[self.tail] = value
            self.head = self.tail
        else:
            if self.isFull():
                return False
            else:
                self.tail = (self.tail + 1) % self.k
                self.queue[self.tail] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            # self.size -= 1
            self.queue[self.head] = -1
            self.head += 1
            self.head = self.head % self.k
            return True

    def Front(self) -> int:
        return self.queue[self.head]

    def Rear(self) -> int:
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.queue[self.head] == -1

    def isFull(self) -> bool:
        return (self.tail + 1) % self.k == self.head and self.queue[self.head] != -1


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(7)
param_1 = obj.enQueue(34)
param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()