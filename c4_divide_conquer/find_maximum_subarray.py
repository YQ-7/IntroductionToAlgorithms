# -*- coding: utf-8 -*-
"""
    最大子数组问题：寻找数组A[low..right]中和最大的非空子数组A[i..j]
"""
import unittest


def find_maximum_subarray_1(arr, low, high):
    """
        方法一
        通过分治算法求解
        时间复杂度：Θ(nlgn)
    """
    if low == high:
        # 基本情况
        return low, high, arr[low]
    # 以中点划分问题
    mid = (low + high) // 2
    # 求左子数组
    left_low, left_high, left_sum = find_maximum_subarray_1(arr, low, mid)
    # 求右子数组
    right_low, right_high, right_sum = find_maximum_subarray_1(arr, mid + 1, high)
    # 求跨中点子数组
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(arr, low, mid, high)
    # 合并问题解
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


def find_max_crossing_subarray(arr, low, mid, high):
    """
        寻找跨中点的和最大子数组
    """
    left_sum = None
    max_left = None
    add_sum = 0
    for i in range(mid, low - 1, -1):
        add_sum += arr[i]
        if left_sum is None or add_sum > left_sum:
            left_sum = add_sum
            max_left = i

    right_sum = None
    max_right = None
    add_sum = 0
    for i in range(mid + 1, high + 1):
        add_sum += arr[i]
        if right_sum is None or add_sum > right_sum:
            right_sum = add_sum
            max_right = i

    return max_left, max_right, left_sum + right_sum


def find_maximum_subarray_2(arr):
    """
        方法二
        时间复杂度：Θ(n)
    """
    max_sum = 0
    max_left = None
    max_right = None
    cur_sum = 0
    cur_left = 0
    for i in range(len(arr)):
        if cur_sum == 0:
            cur_left = i
        cur_sum += arr[i]
        if cur_sum > max_sum:
            max_sum = cur_sum
            max_left = cur_left
            max_right = i
        if cur_sum < 0:
            cur_sum = 0
    return max_left, max_right, max_sum


class MyTestCase(unittest.TestCase):
    def test_find_maximum_subarray_1(self):
        arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
        left, right, max_sum = find_maximum_subarray_1(arr, 0, len(arr) - 1)
        self.assertEqual(7, left)
        self.assertEqual(10, right)
        self.assertEqual(43, max_sum)

    def test_find_maximum_subarray_2(self):
        arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
        left, right, max_sum = find_maximum_subarray_2(arr)
        self.assertEqual(7, left)
        self.assertEqual(10, right)
        self.assertEqual(43, max_sum)


if __name__ == '__main__':
    unittest.main()
