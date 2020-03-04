# -*- coding: utf-8 -*-

import unittest
import utils.random_utils as random_utils
import utils.array_utils as array_utils


# 快速排序
# 最坏时间复杂度：Θ(n^2)
# 期望时间复杂度：Θ(nlgn)
def quick_sort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quick_sort(array, p, q - 1)
        quick_sort(array, q + 1, r)


def partition(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r, 1):
        if array[j] <= x:
            i += 1
            array_utils.exchange(array, i, j)
    array_utils.exchange(array, i + 1, r)
    return i + 1


# 递减排序
def partition_by_desc(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r, 1):
        if array[j] >= x:
            i += 1
            array_utils.exchange(array, i, j)
    array_utils.exchange(array, i + 1, r)
    return i + 1


def randomized_partition(array, p, r):
    """
        随机选择主元版
    """
    i = random_utils.random_int(p, r)
    array_utils.exchange(array, i, r)
    return partition(array, p, r)


def randomized_quick_sort(array, p, r):
    if p < r:
        q = randomized_partition(array, p, r)
        quick_sort(array, p, q - 1)
        quick_sort(array, q + 1, r)


class QuickSort(unittest.TestCase):

    def test_quick_sort(self):
        array = [6, 2, -4, 12, 65, 2]
        quick_sort(array, 0, len(array) - 1)
        self.assertEqual(-4, array[0])
        self.assertEqual(2, array[1])
        self.assertEqual(65, array[5])

    def test_randomized_quick_sort(self):
        array = [6, 2, -4, 12, 65, 2]
        randomized_quick_sort(array, 0, len(array) - 1)
        self.assertEqual(-4, array[0])
        self.assertEqual(2, array[1])
        self.assertEqual(65, array[5])


if __name__ == '__main__':
    unittest.main()
