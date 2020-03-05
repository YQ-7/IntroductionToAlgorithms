# -*- coding: utf-8 -*-
"""
    查询最大值和最小值
"""
import unittest


def get_min_max(arr):
    arr_len = len(arr)
    start = 0 if arr_len % 2 == 0 else 1
    minimum = arr[0]
    maximum = arr[0]
    for i in range(start, arr_len, 2):
        min_i, max_i = (i, i + 1) if arr[i] < arr[i + 1] else (i + 1, i)
        maximum = arr[max_i] if arr[max_i] > maximum else maximum
        minimum = arr[min_i] if arr[min_i] < minimum else minimum

    return minimum, maximum


class MyTestCase(unittest.TestCase):
    def test_get_min_max(self):
        self.assertEqual((0, 0), get_min_max([0]))
        self.assertEqual((0, 2), get_min_max([0, 2, 1]))
        self.assertEqual((-2, 10), get_min_max([0, 2, 1, -2, 9, 10]))


if __name__ == '__main__':
    unittest.main()
