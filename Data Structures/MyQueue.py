"""
    Circular Queue Implementation (Integers)
    Modulo operator usage src:
        https://www.youtube.com/watch?v=ia__kyuwGag
"""
from Queue import Queue


class MyCircularQueue(Queue):

    def __init__(self, arr_size):
        self.arr_size = arr_size
        self.queue = [None for x in range(self.arr_size)]
        self.size = 0
        self.head = 0
        self.tail = 0

    def enqueue(self, num):
        if not self.is_full():
            self.queue[self.tail] = num
            self.tail = (self.tail + 1) % self.arr_size
            self.size += 1

    def dequeue(self):
        if not self.is_empty():
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.arr_size
            self.size -= 1

    def peek(self):
        return self.queue[self.head]

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def is_full(self):
        if not self.is_empty():
            if self.size == self.arr_size:
                return True
        return False

    def get_queue(self):
        return self.queue


if __name__ == '__main__':
    ###########
    # Testing #
    ###########

    myqueue = MyCircularQueue(7)

    # Test - DeQueue empty queue
    myqueue.dequeue()

    # Test - EnQueue
    myqueue.enqueue(1)
    myqueue.enqueue(2)
    myqueue.enqueue(3)
    myqueue.enqueue(4)
    myqueue.enqueue(5)
    myqueue.enqueue(6)
    myqueue.enqueue(7)
    myqueue.enqueue(8)

    # Test - DeQueue
    myqueue.dequeue()

    myqueue.enqueue(8)

    # Test - Overfilling Queue

    print myqueue.get_queue()
