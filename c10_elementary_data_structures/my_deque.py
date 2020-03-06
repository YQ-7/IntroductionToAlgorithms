# -*- coding: utf-8 -*-

import unittest


class Deque(object):

    def __init__(self, length=10):
        self.items = [None] * length
        self.length = length
        self.head = None
        self.tail = 0

    def push(self, item):
        if self.tail == self.head:
            raise OverflowError("overflow")
        self.items[self.tail] = item
        if self.head is None:
            self.head = self.tail

        self.tail = (self.tail + 1) % self.length

    def unshift(self, item):
        if self.tail == self.head:
            raise OverflowError("overflow")

        if self.head is None:
            self.head = self.tail

        self.head = (self.head - 1 + self.length) % self.length
        self.items[self.head] = item

    def pop(self):
        if self.head is None:
            raise OverflowError("underflow")

        self.tail = (self.tail - 1) % self.length
        item = self.items[self.tail]
        self.items[self.tail] = None

        if self.head == self.tail:
            self.head = None
        return item

    def shift(self):
        if self.head is None:
            raise OverflowError("underflow")
        item = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.length

        if self.head == self.tail:
            self.head = None
        return item

    def size(self):
        if self.head is None:
            return 0
        if self.tail > self.head:
            return self.tail - self.head
        else:
            return self.length - self.head + self.tail

    def is_empty(self):
        return self.head is None


class TestDeQue(unittest.TestCase):

    def test_deque(self):
        my_queue = Deque(length=3)
        self.assertTrue(my_queue.is_empty())
        self.assertEqual(0, my_queue.size())
        self.assertRaisesRegex(OverflowError, "underflow", my_queue.pop)
        my_queue.push(1)
        my_queue.push(2)
        my_queue.unshift(-1)
        self.assertFalse(my_queue.is_empty())
        self.assertEqual(3, my_queue.size())
        self.assertRaisesRegex(OverflowError, "overflow", my_queue.push, 3)
        self.assertRaisesRegex(OverflowError, "overflow", my_queue.unshift, 3)
        self.assertEqual(-1, my_queue.shift())
        self.assertEqual(2, my_queue.pop())
        self.assertEqual(1, my_queue.size())
        self.assertEqual(1, my_queue.pop())


if __name__ == '__main__':
    unittest.main()
