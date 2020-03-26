# -*- coding: utf-8 -*-

import unittest

# 钢铁价格表，长度--价格
price = {
    1: 1,
    2: 5,
    3: 8,
    4: 9,
    5: 10,
    6: 17,
    7: 17,
    8: 20,
    9: 24,
    10: 30
}


# 自顶向下递归实现
# 相同子问题会被重复求解
# 时间复杂度: 2 ^ n
def cut_rod(n):
    if n == 0:
        return 0
    q = 0
    for i in range(1, n + 1):
        q = max(q, price[i] + cut_rod(n - i))
    return q


# 带备忘的自顶向下实现
# 相同子问题只求解一次，保存在数组中
#  时间复杂度: n ^ 2
def memoized_cut_rod(n):
    mem_r = [-1] * (n + 1)
    return memoized_cut_rod_aux(n, mem_r)


def memoized_cut_rod_aux(n, mem_r):
    if mem_r[n] >= 0:
        return mem_r[n]
    else:
        q = 0
        for i in range(1, n + 1):
            q = max(q, price[i] + memoized_cut_rod_aux(n - i, mem_r))
    mem_r[n] = q
    return q


# 带备忘的自顶向下实现
# 相同子问题只求解一次，保存在数组中
#  时间复杂度: n ^ 2
def extended_memoized_cut_rod(n):
    mem_r = [-1] * (n + 1)
    s = [0] * (n + 1)
    extended_memoized_cut_rod_aux(n, mem_r, s)
    return mem_r, s


def extended_memoized_cut_rod_aux(n, mem_r, s):
    if mem_r[n] >= 0:
        return mem_r[n]
    else:
        q = 0
        for i in range(1, n + 1):
            if q < price[i] + extended_memoized_cut_rod_aux(n - i, mem_r, s):
                q = price[i] + extended_memoized_cut_rod_aux(n - i, mem_r, s)
                s[n] = i
    mem_r[n] = q
    return q


# 自低向上实现
# 相同子问题只求解一次，保存在数组中
# 时间复杂度: n ^ 2
def bottom_cut_rod(n):
    mem_r = [0] * (n + 1)
    for j in range(1, n + 1):
        q = 0
        for i in range(1, j + 1):
            q = max(q, price[i] + mem_r[j - i])
        mem_r[j] = q
    return mem_r[n]


# 自低向上实现
# 相同子问题只求解一次，保存在数组中
# 返回最优解的切割方式
# 时间复杂度: n ^ 2
def extended_bottom_cut_rod(n):
    mem_r = [0] * (n + 1)
    s = [0] * (n + 1)
    for j in range(1, n + 1):
        q = 0
        for i in range(1, j + 1):
            if q < price[i] + mem_r[j - i]:
                q = price[i] + mem_r[j - i]
                s[j] = i
        mem_r[j] = q
    return mem_r, s


def print_cut_rod_solution(n, s):
    while n > 0:
        print(s[n])
        n = n - s[n]


class SplitSteel(unittest.TestCase):

    def test_cut_rod(self):
        self.assertEqual(0, cut_rod(0))
        self.assertEqual(1, cut_rod(1))
        self.assertEqual(5, cut_rod(2))
        self.assertEqual(10, cut_rod(4))
        self.assertEqual(30, cut_rod(10))

    def test_memoized_cut_rod(self):
        self.assertEqual(0, memoized_cut_rod(0))
        self.assertEqual(1, memoized_cut_rod(1))
        self.assertEqual(5, memoized_cut_rod(2))
        self.assertEqual(10, memoized_cut_rod(4))
        self.assertEqual(30, memoized_cut_rod(10))

    def test_bottom_cut_rod(self):
        self.assertEqual(0, bottom_cut_rod(0))
        self.assertEqual(1, bottom_cut_rod(1))
        self.assertEqual(5, bottom_cut_rod(2))
        self.assertEqual(10, bottom_cut_rod(4))
        self.assertEqual(30, bottom_cut_rod(10))

    def test_print_bottom_cut_rod_solution(self):
        (r, s) = extended_bottom_cut_rod(10)
        self.assertTrue(10 in s)
        print_cut_rod_solution(10, s)
        (r, s) = extended_bottom_cut_rod(9)
        print_cut_rod_solution(9, s)
        self.assertTrue(3, 6 in s)

    def test_print_extended_memoized_cut_rod_solution(self):
        (r, s) = extended_memoized_cut_rod(10)
        self.assertTrue(10 in s)
        print_cut_rod_solution(10, s)
        (r, s) = extended_memoized_cut_rod(9)
        print_cut_rod_solution(9, s)
        self.assertTrue(3, 6 in s)


if __name__ == '__main__':
    unittest.main()
