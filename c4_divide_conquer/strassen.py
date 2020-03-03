# -*- coding: utf-8 -*-
"""
    strassen算法求解两矩阵乘积
    时间复制度：Θ(n^lg7)
"""
import unittest


def matrix_add(a, b):
    return [[a[i][j] + b[i][j]
             for j in range(len(a[i]))]
            for i in range(len(a))]


def matrix_minus(a, b):
    return [[a[i][j] - b[i][j]
             for j in range(len(a[i]))]
            for i in range(len(a))]


def matrix_divide(a, start_r, start_c, end_r, end_c):
    return [[a[i][j]
             for j in range(start_c, end_c + 1)]
            for i in range(start_r, end_r + 1)]


def matrix_merge(top_left, top_right, bot_left, bot_right):
    res = []
    for i in range(len(top_left)):
        res.append(top_left[i] + top_right[i])
    for i in range(len(bot_left)):
        res.append(bot_left[i] + bot_right[i])
    return res


def strassen(a, b):
    # 基本情况
    if len(a) == 1:
        return [[a[0][0] * b[0][0]]]

    # 分解矩阵
    size = len(a)
    new_size = len(a) // 2
    a11 = matrix_divide(a, 0, 0, new_size - 1, new_size - 1)
    a12 = matrix_divide(a, 0, new_size, new_size - 1, size - 1)
    a21 = matrix_divide(a, new_size, 0, size - 1, new_size - 1)
    a22 = matrix_divide(a, new_size, new_size, size - 1, size - 1)

    b11 = matrix_divide(b, 0, 0, new_size - 1, new_size - 1)
    b12 = matrix_divide(b, 0, new_size, new_size - 1, size - 1)
    b21 = matrix_divide(b, new_size, 0, size - 1, new_size - 1)
    b22 = matrix_divide(b, new_size, new_size, size - 1, size - 1)

    # 通过和或差就出s1~s10
    s1 = matrix_minus(b12, b22)
    s2 = matrix_add(a11, a12)
    s3 = matrix_add(a21, a22)
    s4 = matrix_minus(b21, b11)
    s5 = matrix_add(a11, a22)
    s6 = matrix_add(b11, b22)
    s7 = matrix_minus(a12, a22)
    s8 = matrix_add(b21, b22)
    s9 = matrix_minus(a11, a21)
    s10 = matrix_add(b11, b12)

    # 递归求解子问题
    p1 = strassen(a11, s1)
    p2 = strassen(s2, b22)
    p3 = strassen(s3, b11)
    p4 = strassen(a22, s4)
    p5 = strassen(s5, s6)
    p6 = strassen(s7, s8)
    p7 = strassen(s9, s10)

    # 合并子问题的解
    c11 = matrix_add(matrix_add(p5, p4), matrix_minus(p6, p2))
    c12 = matrix_add(p1, p2)
    c21 = matrix_add(p3, p4)
    c22 = matrix_add(matrix_minus(p5, p3), matrix_minus(p1, p7))
    return matrix_merge(c11, c12, c21, c22)


class MyTestCase(unittest.TestCase):
    def test_strassen(self):
        a = [
            [10, 9, 4, 3],
            [8, 3, 4, 1],
            [93, 1, 9, 3],
            [2, 2, 7, 6]
        ]

        b = [
            [4, 5, 3, 5],
            [4, 1, 2, 1],
            [9, 8, 3, 5],
            [6, 3, 7, 9]
        ]

        expect = [[130, 100, 81, 106],
                  [86, 78, 49, 72],
                  [475, 547, 329, 538],
                  [115, 86, 73, 101]]

        c = strassen(a, b)
        self.assertEqual(expect, c)


if __name__ == '__main__':
    unittest.main()
