# -*- coding: utf-8 -*-

import unittest


class Queue(object):

    def __init__(self, length=50):
        self.items = [None] * (length + 1)  # 额外的一个位置方便用来判断队列是否已满
        self._length = length + 1
        self.head = 0  # 指向队头元素
        self.tail = 0  # 指向下一个新元素将要插入的位置

    def enqueue(self, item):
        if self.head == (self.tail + 1) % self._length:
            raise OverflowError("Queue overflow")
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self._length

    def dequeue(self):
        if self.is_empty():
            raise OverflowError("Queue underflow")
        item = self.items[self.head]
        self.head = (self.head + 1) % self._length
        return item

    def size(self):
        if self.is_empty():
            return 0
        if self.tail > self.head:
            return self.tail - self.head
        else:
            return self._length - self.head + self.tail

    def is_empty(self):
        return self.head == self.tail


class TestQueue(unittest.TestCase):

    def test_queue(self):
        my_queue = Queue(length=3)
        self.assertTrue(my_queue.is_empty())
        self.assertEqual(0, my_queue.size())
        self.assertRaisesRegex(OverflowError, "Queue underflow", my_queue.dequeue)
        my_queue.enqueue(1)
        my_queue.enqueue(2)
        my_queue.enqueue(3)
        self.assertRaisesRegex(OverflowError, "Queue overflow", my_queue.enqueue, 4)
        self.assertEqual(3, my_queue.size())
        self.assertFalse(my_queue.is_empty())
        self.assertEqual(1, my_queue.dequeue())
        self.assertEqual(2, my_queue.dequeue())
        self.assertEqual(3, my_queue.dequeue())
        my_queue.enqueue(11)
        my_queue.enqueue(12)
        self.assertEqual(2, my_queue.size())
        self.assertEqual(11, my_queue.dequeue())
        self.assertEqual(12, my_queue.dequeue())


if __name__ == '__main__':
    unittest.main()
