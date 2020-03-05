# -*- coding: utf-8 -*-
"""
    最坏情况下为线性时间的选择算法
"""
import unittest
import math
from utils import array_utils


def select_main(arr, i):
    return select(arr, 0, len(arr) - 1, i)


def select(arr, p, r, i):
    """
    :param arr: 数组集合
    :param p: 数组区间开始位置
    :param r: 数组区间结束位置
    :param i: 第i小顺序量，以1开始
    :return: 第i小顺序量值
    """
    if p == r:
        return arr[p]
    n = r - p + 1
    # 将arr[p..r]分为n/5组，每组5个元素，最后一组n % 5个元素
    groups = []
    group_num = math.ceil(n / 5)
    for j in range(group_num - 1):
        g = arr[p + j * 5: p + j * 5 + 5]
        groups.append(g)
    groups.append(arr[p + (group_num - 1) * 5: r + 1])

    # 寻找每组的中位数
    medians = []
    for g in groups:
        # 先分别将每组数据排序，再找中文数
        medians.append(insertion_sort(g)[(len(g) + 1) // 2 - 1])

    # 寻找中位数组的中位数
    x = select(medians, 0, len(medians) - 1, (len(medians) + 1) // 2)

    # 以x为主元划分数组
    q = partition(arr, p, r, x)

    k = q - p + 1
    if i == k:
        # 找到第i小顺序量
        return x
    if i < k:
        # 第i小顺序量在低区
        return select(arr, p, q - 1, i)
    # 第i小顺序量在高区
    return select(arr, q + 1, r, i - k)


def partition(arr, p, r, x):
    # 先将主元x放置到位置r处
    for j in range(p, r + 1):
        if arr[j] == x:
            array_utils.exchange(arr, j, r)
            break
    i = p - 1
    for j in range(p, r, 1):
        if arr[j] <= x:
            i += 1
            array_utils.exchange(arr, i, j)
    array_utils.exchange(arr, i + 1, r)
    return i + 1


def insertion_sort(arr):
    """
        插入排序
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


class MyTestCase(unittest.TestCase):
    def test_select(self):
        self.assertEqual(1, select_main([5, 2, 1, 6, 3, 4, 12, 10, 7, 9, 8, 11], 1))
        self.assertEqual(3, select_main([5, 2, 1, 6, 3, 4, 12, 10, 7, 9, 8, 11], 3))
        self.assertEqual(6, select_main([5, 2, 1, 6, 3, 4, 12, 10, 7, 9, 8, 11], 6))
        self.assertEqual(12, select_main([5, 2, 1, 6, 3, 4, 12, 10, 7, 9, 8, 11], 12))


if __name__ == '__main__':
    unittest.main()
