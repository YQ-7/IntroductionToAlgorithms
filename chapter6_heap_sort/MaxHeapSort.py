# -*- coding: utf-8 -*-

import unittest
import utils.random_utils as random_utils


class MaxHeapSort(unittest.TestCase):

    # 获取左孩子节点
    @staticmethod
    def left(i):
        return 2 * i + 1

    # 获取右孩子节点
    @staticmethod
    def right(i):
        return 2 * i + 2

    # 最大堆辅助函数：确保i元素大于它的子节点
    # 运行时间O(lgN)
    @staticmethod
    def max_heapify(array, i, heap_size):
        l = MaxHeapSort.left(i)
        r = MaxHeapSort.right(i)
        largest = i
        if l < heap_size and array[l] > array[i]:
            largest = l
        if r < heap_size and array[r] > array[largest]:
            largest = r
        if largest != i:
            MaxHeapSort.exchange(array, i, largest)
            MaxHeapSort.max_heapify(array, largest, heap_size)

    # 最大堆辅助函数：确保i元素大于它的子节点
    # 运行时间O(lgN)
    # 循环版本
    @staticmethod
    def max_heapify_while(array, i, heap_size):
        while True:
            l = MaxHeapSort.left(i)
            r = MaxHeapSort.right(i)
            largest = i
            if l < heap_size and array[l] > array[i]:
                largest = l
            if r < heap_size and array[r] > array[largest]:
                largest = r
            if largest != i:
                MaxHeapSort.exchange(array, i, largest)
                i = largest
            else:
                break

    @staticmethod
    def exchange(array, i, j):
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp

    # 构建最大堆
    # 运行时间O(N)
    @staticmethod
    def build_max_heap(array, heap_size):
        for i in range((heap_size // 2) - 1, -1, -1):
            # HeapSort.max_heapify(array, i, heap_size)
            MaxHeapSort.max_heapify_while(array, i, heap_size)

    # 堆排序，按升序顺寻排序
    # 运行时间O(NlgN)
    @staticmethod
    def heap_sort(array):
        heap_size = len(array)
        MaxHeapSort.build_max_heap(array, heap_size)
        for i in range(len(array) - 1, 0, -1):
            MaxHeapSort.exchange(array, 0, i)
            heap_size -= 1
            # HeapSort.max_heapify(array, 0, heap_size)
            MaxHeapSort.max_heapify_while(array, 0, heap_size)

    def test_hear_sort(self):
        array = random_utils.random_int_list()
        self.heap_sort(array)
        print(array)
