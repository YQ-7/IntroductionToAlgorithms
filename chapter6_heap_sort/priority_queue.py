# -*- coding: utf-8 -*-

import unittest
import sys
import chapter6_heap_sort.max_heap_sort as max_heap_sort
import utils.array_utils as array_utils
import utils.random_utils as random_utils

# 优先队列


# 返回队列中最大的元素
# 运行时间：Θ(1)
def maximum(queue):
    return queue[0]


# 移除并去掉队列中最元素
# 运行时间：O(lgN)
def extract_max(queue):
    if len(queue) < 1:
        print("queue is empty")
        return
    max_item = queue[0]
    heap_size = len(queue)
    queue[0] = queue[heap_size - 1]
    queue.pop()
    max_heap_sort.max_heapify(queue, 0, heap_size - 1)
    return max_item


# 将元素x的关键字值增加到key
# 运行时间：O(lgN)
def heap_increase_key(queue, x, key):
    if key < queue[x]:
        print("new key is smaller than current key")
        return
    queue[x] = key
    while x > 0 and queue[max_heap_sort.parent(x)] < queue[x]:
        array_utils.exchange(queue, max_heap_sort.parent(x), x)
        x = max_heap_sort.parent(x)


# 向队列中插入元素key
# 运行时间: O(lgN)
def insert(queue, key):
    queue.append(-sys.maxsize-1)
    heap_increase_key(queue, len(queue) - 1, key)


class PriorityQueue(unittest.TestCase):

    @staticmethod
    def test_priority_queue():
        priority_queue = random_utils.random_int_list()
        max_heap_sort.build_max_heap(priority_queue, len(priority_queue))
        print("priority_queue: ",  priority_queue)
        print("get max: ",  maximum(priority_queue))
        print("extract max: ",  extract_max(priority_queue))
        print("priority_queue: ", priority_queue)
        new_key = priority_queue[4] + random_utils.random_int(1, 100)
        print("increase item 5: %d to %d" % (priority_queue[4], new_key))
        heap_increase_key(priority_queue, 4, new_key)
        print("priority_queue: ", priority_queue)
        insert_key = random_utils.random_int()
        print("increase key: %d" % (insert_key,))
        insert(priority_queue, insert_key)
        print("priority_queue: ", priority_queue)
