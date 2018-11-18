# -*- coding: utf-8 -*-

import unittest


# 2.1-4
# 2个n位二级制数相加，结果按二级制形式存放在(n+1)数组中
def binary_add(a, b):
    # 进位标志位
    flag = 0
    c = [0] * (len(a) + 1)
    for i in range(len(a)):
        r = a[i] + b[i] + flag
        c[i] = r % 2
        flag = r // 2
    if flag == 1:
        c[len(a)] = 1
    return c


class BinaryAdd(unittest.TestCase):

    @staticmethod
    def test_binary_add():
        a = [1, 0, 1, 1, 0]
        b = [1, 1, 1, 1, 1]
        c = binary_add(a, b)
        print(c)
