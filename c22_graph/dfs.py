# -*- coding: utf-8 -*-

"""
    深度优先搜索算法
"""
import unittest
from enum import Enum


class Color(Enum):
    WHITE = 0  # 未发现节点
    GRAY = 1  # 已发现，但邻接节点可能存在未发现几点
    BLACK = 2  # 已发现，邻接节点均已发现


class Node(object):

    def __init__(self, data):
        self.data = data  # 数据
        self.parent = None  # 前驱节点
        self.color = None  # 节点探索状态
        self.d = None  # 首次发现时间
        self.f = None  # 节点处理完成时间


def dfs(graph):
    """
        时间复杂度：O(V+E)，V：顶点数，E：边数
    """
    # 初始化节点
    for u in graph:
        u.color = Color.WHITE
        u.parent = None
    time = [0]
    for u in graph:
        if u.color == Color.WHITE:
            dfs_visit(graph, u, time)


def dfs_visit(graph, u, time):
    time[0] += 1
    u.d = time[0]
    u.color = Color.GRAY
    for v in graph[u]:
        if v.color == Color.WHITE:
            v.parent = u
            dfs_visit(graph, v, time)
    u.color = Color.BLACK
    time[0] += 1
    u.f = time[0]


class MyTestCase(unittest.TestCase):
    def test_dfs(self):
        n1 = Node("u")
        n2 = Node("v")
        n3 = Node("x")
        n4 = Node("y")
        n5 = Node("w")
        n6 = Node("z")

        graph = {
            n1: [n2, n3],
            n2: [n4],
            n3: [n2],
            n4: [n3],
            n5: [n4, n6],
            n6: [n6]
        }

        dfs(graph)
        self.assertEqual(1, n1.d)
        self.assertEqual(8, n1.f)
        self.assertEqual(2, n2.d)
        self.assertEqual(7, n2.f)
        self.assertEqual(10, n6.d)
        self.assertEqual(11, n6.f)


if __name__ == '__main__':
    unittest.main()
