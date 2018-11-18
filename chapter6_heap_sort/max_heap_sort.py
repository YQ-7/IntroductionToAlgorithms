# -*- coding: utf-8 -*-

import unittest
import utils.random_utils as random_utils


# 获取左孩子节点
def left(i):
    return 2 * i + 1


# 获取右孩子节点
def right(i):
    return 2 * i + 2


# 最大堆辅助函数：确保i元素大于它的子节点
# 运行时间O(lgN)
def max_heapify(array, i, heap_size):
    l = left(i)
    r = right(i)
    largest = i
    if l < heap_size and array[l] > array[i]:
        largest = l
    if r < heap_size and array[r] > array[largest]:
        largest = r
    if largest != i:
        exchange(array, i, largest)
        max_heapify(array, largest, heap_size)


# 最大堆辅助函数：确保i元素大于它的子节点
# 运行时间O(lgN)
# 循环版本
def max_heapify_while(array, i, heap_size):
    while True:
        l = left(i)
        r = right(i)
        largest = i
        if l < heap_size and array[l] > array[i]:
            largest = l
        if r < heap_size and array[r] > array[largest]:
            largest = r
        if largest != i:
            exchange(array, i, largest)
            i = largest
        else:
            break


def exchange(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


# 构建最大堆
# 运行时间O(N)
def build_max_heap(array, heap_size):
    for i in range((heap_size // 2) - 1, -1, -1):
        # max_heapify(array, i, heap_size)
        max_heapify_while(array, i, heap_size)


# 堆排序，按升序顺寻排序
# 运行时间O(NlgN)
def heap_sort(array):
    heap_size = len(array)
    build_max_heap(array, heap_size)
    for i in range(len(array) - 1, 0, -1):
        exchange(array, 0, i)
        heap_size -= 1
        # max_heapify(array, 0, heap_size)
        max_heapify_while(array, 0, heap_size)


class MaxHeapSort(unittest.TestCase):
    
    @staticmethod
    def test_hear_sort():
        array = random_utils.random_int_list()
        heap_sort(array)
        print(array)
