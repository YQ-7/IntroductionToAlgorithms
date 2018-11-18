# -*- coding: utf-8 -*-

import unittest
import utils.random_utils as random_utils


# 插入排序:时间复杂度Θ(n^2)
# acs=True:升序排序
# acs=False:降序排序
def insertion_sort(array, asc=True):
    for i in range(len(array)):
        if i == 0:
            continue
        current_num = array[i]
        last_index = i - 1
        while last_index >= 0 and compare_by_asc(current_num, array[last_index], asc):
            array[last_index + 1] = array[last_index]
            last_index -= 1
        array[last_index + 1] = current_num


def compare_by_asc(num_a, num_b, asc):
    if asc:
        return num_a < num_b
    else:
        return num_a > num_b


class InsertionSort(unittest.TestCase):

    @staticmethod
    def test_insertion_sort_by_asc():
        array = random_utils.random_int_list()
        # 升序排序
        insertion_sort(array)
        print(array)
        # 降序排序
        insertion_sort(array, asc=False)
        print(array)
