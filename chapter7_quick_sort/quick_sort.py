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


#递减排序
def partition_by_desc(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r, 1):
        if array[j] >= x:
            i += 1
            array_utils.exchange(array, i, j)
    array_utils.exchange(array, i + 1, r)
    return i + 1


class QuickSort(unittest.TestCase):

    @staticmethod
    def test_quick_sort():
        array = random_utils.random_int_list()
        quick_sort(array, 0, len(array) - 1)
        print(array)
