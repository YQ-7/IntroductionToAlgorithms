# -*- coding: utf-8 -*-

import unittest
import random


class InsertionSort(unittest.TestCase):

    # 插入排序:时间复杂度O(n^2)
    # acs=True:升序排序
    # acs=False:降序排序
    @staticmethod
    def insertion_sort(array, asc=True):
        for i in range(len(array)):
            if i == 0:
                continue
            current_num = array[i]
            last_index = i - 1
            while last_index >= 0 and InsertionSort.compare_by_asc(current_num, array[last_index], asc):
                array[last_index + 1] = array[last_index]
                last_index -= 1
            array[last_index + 1] = current_num

    @staticmethod
    def compare_by_asc(num_a, num_b, asc):
        if asc:
            return num_a < num_b
        else:
            return num_a > num_b

    # 产生随机数组
    @staticmethod
    def random_int_list(start=0, stop=1000, length=10):
        start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
        length = int(abs(length)) if length else 0
        random_list = []
        for i in range(length):
            random_list.append(random.randint(start, stop))
        return random_list

    def test_insertion_sort_by_asc(self):
        array = self.random_int_list()
        # 升序排序
        self.insertion_sort(array)
        print(array)
        # 降序排序
        self.insertion_sort(array, asc=False)
        print(array)
