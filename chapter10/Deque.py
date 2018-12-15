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
            print("Queue overflow")
            return
        self.items[self.tail] = item
        if self.head is None:
            self.head = self.tail

        self.tail = (self.tail + 1) % self.length

    def unshift(self, item):
        if self.tail == self.head:
            print("Queue overflow")
            return

        if self.head is None:
            self.head = self.tail

        self.head = (self.head - 1 + self.length) % self.length
        self.items[self.head] = item

    def pop(self):
        if self.head is None:
            print("Queue underflow")
            return

        self.tail = (self.tail - 1) % self.length
        item = self.items[self.tail]
        self.items[self.tail] = None

        if self.head == self.tail:
            self.head = None
        return item

    def shift(self):
        if self.head is None:
            print("Queue underflow")
            return
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

    @staticmethod
    def test_deque():
        my_queue = Deque(length=3)
        my_queue.push(1)
        my_queue.push(2)
        my_queue.unshift(-1)
        print(my_queue.size())
        print(my_queue.pop())
        print(my_queue.shift())
        print(my_queue.is_empty())
        print(my_queue.pop())
        print(my_queue.is_empty())
