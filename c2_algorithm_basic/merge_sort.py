# -*- coding: utf-8 -*-

"""
归并排序
时间复杂度:Θ(nlgn)
"""
import unittest


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    """
        合并已排序数组arr[left, mid]和arr[mid + 1, right]
    """
    # 复制arr[left, mid] --> left_arr
    left_arr = []
    for i in range(left, mid + 1):
        left_arr.append(arr[i])
    # 复制arr[mid+1, right] --> right_arr
    right_arr = []
    for i in range(mid + 1, right + 1):
        right_arr.append(arr[i])

    # 合并arr[left, mid]和arr[mid + 1, right] --> arr[left, right]
    i = 0
    j = 0
    for k in range(left, right + 1):
        if j >= len(right_arr) or (i < len(left_arr) and left_arr[i] <= right_arr[j]):
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1


class MyTestCase(unittest.TestCase):
    def test_merge_sort(self):
        arr = [5, 2, 4, 7, 1, 3, 2, 6]
        merge_sort(arr, 0, len(arr) - 1)
        self.assertEqual(1, arr[0])
        self.assertEqual(2, arr[1])
        self.assertEqual(4, arr[4])
        self.assertEqual(7, arr[7])


if __name__ == '__main__':
    unittest.main()
