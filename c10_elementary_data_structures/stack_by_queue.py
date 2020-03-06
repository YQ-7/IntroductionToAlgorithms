# -*- coding: utf-8 -*-

import unittest
from utils.my_queue import Queue


class StackByQueue(object):

    def __init__(self, length=10):
        self.a_queue = Queue(length)
        self.b_queue = Queue(length)

    # 判断栈是否为空，返回布尔值
    def is_empty(self):
        return self.a_queue.is_empty() and self.b_queue.is_empty()

    # 入栈
    def push(self, item):
        if not self.a_queue.is_empty():
            self.a_queue.enqueue(item)
        else:
            self.b_queue.enqueue(item)

    # 出栈
    def pop(self):
        if self.is_empty():
            raise OverflowError("underflow")

        if self.a_queue.is_empty():
            while self.b_queue.size() > 1:
                self.a_queue.enqueue(self.b_queue.dequeue())
            return self.b_queue.dequeue()
        else:
            while self.a_queue.size() > 1:
                self.b_queue.enqueue(self.a_queue.dequeue())
            return self.a_queue.dequeue()

    def size(self):
        return self.b_queue.size() if self.a_queue.is_empty() else self.a_queue.size()


class TestStack(unittest.TestCase):

    def test_stack(self):
        my_stack = StackByQueue(length=3)
        self.assertTrue(my_stack.is_empty())
        self.assertEqual(0, my_stack.size())
        self.assertRaisesRegex(OverflowError, "underflow", my_stack.pop)
        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)
        self.assertRaisesRegex(OverflowError, "Queue overflow", my_stack.push, 4)
        self.assertFalse(my_stack.is_empty())
        self.assertEqual(3, my_stack.size())
        self.assertEqual(3, my_stack.pop())
        my_stack.push(4)
        self.assertEqual(4, my_stack.pop())
        self.assertEqual(2, my_stack.pop())
        self.assertEqual(1, my_stack.pop())
        self.assertTrue(my_stack.is_empty())
        self.assertEqual(0, my_stack.size())


if __name__ == '__main__':
    unittest.main()
