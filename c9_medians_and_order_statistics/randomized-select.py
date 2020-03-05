# -*- coding: utf-8 -*-
"""
    利用分治算法实现的选择查找
"""
import unittest
from utils import array_utils
from utils import random_utils


def select(arr, i):
    if i < 0 or i > len(arr):
        return None
    return randomized_select(arr, 0, len(arr) - 1, i)


def randomized_select(arr, p, r, i):
    if p == r:
        return arr[r]
    q = randomized_partition(arr, p, r)
    # 主元在此子集合中的顺序量
    k = q - p + 1
    if k == i:
        return arr[q]
    if i < k:
        # 待求顺序量在左子集合
        return randomized_select(arr, p, q - 1, i)
    # 待求顺序量在右子集合
    return randomized_select(arr, q + 1, r, i - k)


def randomized_partition(arr, p, r):
    i = random_utils.random_int(p, r)
    array_utils.exchange(arr, i, r)
    return partition(arr, p, r)


def partition(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r, 1):
        if array[j] <= x:
            i += 1
            array_utils.exchange(array, i, j)
    array_utils.exchange(array, i + 1, r)
    return i + 1


class MyTestCase(unittest.TestCase):
    def test_randomized_select(self):
        self.assertEqual(1, select([5, 2, 1, 6, 3, 4], 1))
        self.assertEqual(3, select([5, 2, 1, 6, 3, 4], 3))
        self.assertEqual(5, select([5, 2, 1, 6, 3, 4], 5))
        self.assertEqual(6, select([5, 2, 1, 6, 3, 4], 6))


if __name__ == '__main__':
    unittest.main()
