# -*- coding: utf-8 -*-

import unittest


class Stack(object):

    def __init__(self, length=100):
        self.items = [None] * length
        self.top = -1

    # 判断栈是否为空，返回布尔值
    def is_empty(self):
        return self.top == -1

    # 入栈
    def push(self, item):
        if self.top == len(self.items) - 1:
            raise OverflowError("overflow")
        self.top += 1
        self.items[self.top] = item

    # 出栈
    def pop(self):
        if self.is_empty():
            raise OverflowError("underflow")
        self.top -= 1
        return self.items[self.top + 1]

    def size(self):
        return len(self.items)


class MyTestCase(unittest.TestCase):
    def test_select(self):
        my_stack = Stack(size=3)
        self.assertTrue(my_stack.is_empty())
        self.assertRaisesRegex(OverflowError, "underflow", my_stack.pop)
        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)
        self.assertRaisesRegex(OverflowError, "overflow", my_stack.push, 4)
        self.assertEqual(3, my_stack.pop())
        self.assertFalse(my_stack.is_empty())
        self.assertEqual(2, my_stack.pop())
        self.assertEqual(1, my_stack.pop())
        self.assertTrue(my_stack.is_empty())


if __name__ == '__main__':
    unittest.main()
