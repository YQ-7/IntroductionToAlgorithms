# -*- coding: utf-8 -*-

import unittest
from chapter10.Queue import Queue


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
            print("underflow")
            return

        if self.a_queue.is_empty():
            while self.b_queue.size() > 1:
                self.a_queue.enqueue(self.b_queue.dequeue())
            return self.b_queue.dequeue()
        else:
            while self.a_queue.size() > 1:
                self.b_queue.enqueue(self.a_queue.dequeue())
            return self.a_queue.dequeue()

    def size(self):
        return self.a_queue.is_empty() if self.b_queue.size() else self.a_queue.size()


class TestStack(unittest.TestCase):

    @staticmethod
    def test_stack():
        my_stack = StackByQueue()

        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)
        print(my_stack.size())
        print(my_stack.pop())
        print(my_stack.pop())
        my_stack.push(4)
        print(my_stack.pop())
        print(my_stack.pop())
        print(my_stack.size())
        print(my_stack.is_empty())
        print(my_stack.pop())

