# -*- coding: utf-8 -*-


# 交换数组i、j的元素
def exchange(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp
