# -*- coding: utf-8 -*-

import unittest
from utils.my_stack import Stack


class QueueByStack(object):

    def __init__(self, length=100):
        self.push_stack = Stack(length=length)
        self.pop_stack = Stack(length=length)

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

    def test_stack(self):
        my_queue = QueueByStack()
        self.assertTrue(my_queue.is_empty())
        my_queue.enqueue(1)
        my_queue.enqueue(2)
        my_queue.enqueue(3)
        self.assertFalse(my_queue.is_empty())
        my_queue.enqueue(4)
        self.assertEqual(1, my_queue.dequeue())
        self.assertEqual(2, my_queue.dequeue())
        self.assertEqual(3, my_queue.dequeue())
        self.assertEqual(4, my_queue.dequeue())
        self.assertTrue(my_queue.is_empty())


if __name__ == '__main__':
    unittest.main()
