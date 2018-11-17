# -*- coding: utf-8 -*-

import unittest
import utils.random_utils as random_utils


class MinHeapSort(unittest.TestCase):

    # 获取左孩子节点
    @staticmethod
    def left(i):
        return 2 * i + 1

    # 获取右孩子节点
    @staticmethod
    def right(i):
        return 2 * i + 2

    # 最小堆辅助函数：确保i元素小于它的子节点
    # 运行时间O(lgN)
    @staticmethod
    def min_heapify(array, i, heap_size):
        l = MinHeapSort.left(i)
        r = MinHeapSort.right(i)
        smallest = i
        if l < heap_size and array[l] < array[i]:
            smallest = l
        if r < heap_size and array[r] < array[smallest]:
            smallest = r
        if smallest != i:
            MinHeapSort.exchange(array, i, smallest)
            MinHeapSort.min_heapify(array, smallest, heap_size)

    @staticmethod
    def exchange(array, i, j):
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp

    # 构建最小堆
    # 运行时间O(N)
    @staticmethod
    def build_min_heap(array, heap_size):
        for i in range((heap_size // 2) - 1, -1, -1):
            MinHeapSort.min_heapify(array, i, heap_size)

    # 堆排序，按升序顺寻排序
    # 运行时间O(NlgN)
    @staticmethod
    def heap_sort(array):
        heap_size = len(array)
        MinHeapSort.build_min_heap(array, heap_size)
        for i in range(len(array) - 1, 0, -1):
            MinHeapSort.exchange(array, 0, i)
            heap_size -= 1
            MinHeapSort.min_heapify(array, 0, heap_size)

    def test_hear_sort(self):
        array = random_utils.random_int_list()
        self.heap_sort(array)
        print(array)
