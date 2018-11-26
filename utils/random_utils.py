# -*- coding: utf-8 -*-
import random


# 产生随机数组
def random_int_list(start=0, stop=1000, length=10):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


def random_int(start=0, stop=1000):
    return random.randint(start, stop)
