# -*- coding: utf-8 -*-

import unittest
from chapter10.Stack import Stack


class QueueByStack(object):

    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()

    def enqueue(self, item):
        self.push_stack.push(item)

    def dequeue(self):
        if self.pop_stack.is_empty():
            while not self.push_stack.is_empty():
                self.pop_stack.push(self.push_stack.pop())
        return self.pop_stack.pop()

    def is_empty(self):
        return self.pop_stack.is_empty() and self.push_stack.is_empty()


class TestQueueByStack(unittest.TestCase):

    @staticmethod
    def test_stack():
        my_queue = QueueByStack()
        my_queue.enqueue(1)
        my_queue.enqueue(2)
        my_queue.enqueue(3)
        print(my_queue.is_empty())
        my_queue.enqueue(4)
        print(my_queue.dequeue())
        print(my_queue.dequeue())
        print(my_queue.dequeue())
        print(my_queue.dequeue())
        print(my_queue.is_empty())

