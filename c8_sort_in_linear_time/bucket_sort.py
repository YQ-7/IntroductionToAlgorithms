# -*- coding: utf-8 -*-
"""
    桶排序
"""

import unittest


def bucket_sort(arr, bucket_num=5):
    buckets = [None] * bucket_num
    max_v = arr[0]
    min_v = arr[0]
    for v in arr:
        if v > max_v:
            max_v = v
        if v < min_v:
            min_v = v
    # 计数桶间距，+1避免最后一个桶区间末端数据溢出
    space = (max_v - min_v + 1) / bucket_num

    # 将数据放入值所属区间桶中
    for v in arr:
        # 计算元素属于那个桶
        index = int((v - min_v) // space)
        if buckets[index] is None:
            # 桶中首次加入元素
            buckets[index] = [v]
        else:
            # 按从小到大次序放入桶中
            bucket = buckets[index]
            k = len(bucket) - 1
            bucket.append(None)  # 先扩充
            while k >= 0 and bucket[k] > v:
                bucket[k + 1] = bucket[k]
                k -= 1
            bucket[k + 1] = v

    # 合并桶数据
    res = []
    for b in buckets:
        if b is not None:
            res.extend(b)
    return res


class MyTestCase(unittest.TestCase):
    def test_something(self):
        array = [9, 10, 4, 3, -1, 4, 1, 2]
        array = bucket_sort(array)
        self.assertEqual(-1, array[0])
        self.assertEqual(2, array[2])
        self.assertEqual(4, array[5])
        self.assertEqual(10, array[7])


if __name__ == '__main__':
    unittest.main()
