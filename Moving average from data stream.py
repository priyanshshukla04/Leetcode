from collections import deque
class MovingAverage:
    def __init__(self, size:int):
        self.queue = deque()
        self.maxSize = size
        self.sum = 0.0

    def next(self, val: int):
        if len(self.queue) == self.maxSize:
            self.sum -= self.queue.pop()
            self.queue.pop()
        self.queue.append(val)
        self.sum += val
        return self.sum / self.maxSize




obj = MovingAverage(3)
param1 = obj.next(1)
print(param1)
param1 = obj.next(10)
print(param1)
param1 = obj.next(3)
print(param1)
param1 = obj.next(5)
print(param1)