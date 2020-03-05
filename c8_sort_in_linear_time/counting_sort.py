# -*- coding: utf-8 -*-
"""
    计数排序
"""

import unittest


def counting_sort(arr, k):
    count = [0] * (k + 1)
    # 累计每个元素个数
    for i in range(len(arr)):
        count[arr[i]] += 1
    # 确定每个元素在输出数组中的位置
    for i in range(1, k + 1):
        count[i] = count[i] + count[i - 1]
    res = [None] * len(arr)
    # 从后往前将元素放入输出数组，并更新位置计数
    for i in range(len(arr) - 1, -1, -1):
        # 计数从1开始，而输出数组是从0开始，需-1
        res[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    return res


class MyTestCase(unittest.TestCase):
    def test_something(self):
        array = [9, 10, 4, 3, 0, 4, 1, 2]
        array = counting_sort(array, 10)
        self.assertEqual(0, array[0])
        self.assertEqual(2, array[2])
        self.assertEqual(4, array[5])
        self.assertEqual(10, array[7])


if __name__ == '__main__':
    unittest.main()
