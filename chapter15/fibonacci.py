# -*- coding: utf-8 -*-

import unittest


def fibonacci(n):
    if n < 2:
        return 1
    fib = [None] * (n + 1)
    fib[0] = fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]


class Fibonacci(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEquals(1, fibonacci(0))
        self.assertEquals(1, fibonacci(1))
        self.assertEquals(2, fibonacci(2))
        self.assertEquals(3, fibonacci(3))
        self.assertEquals(5, fibonacci(4))