# -*- coding: utf-8 -*-

"""
    广度优先搜索算法
"""
import unittest
from enum import Enum
from utils.my_queue import Queue


class Color(Enum):
    WHITE = 0  # 未发现节点
    GRAY = 1   # 已发现，但邻接节点可能存在未发现几点
    BLACK = 2  # 已发现，邻接节点均已发现


class Node(object):

    def __init__(self, data):
        self.data = data    # 数据
        self.parent = None  # 前驱节点
        self.distance = -1  # 距离源节点的距离
        self.color = None   # 节点探索状态


def bfs(graph, s):
    """
        时间复杂度：O(V+E)，V：顶点数，E：边数
    """
    # 初始化节点
    for u in graph:
        u.color = Color.WHITE
        u.distance = -1
        u.parent = None
    # 设置源节点
    s.color = Color.GRAY
    s.distance = 0
    s.parent = None
    queue = Queue()
    queue.enqueue(s)
    # 从源节点开始搜索
    while not queue.is_empty():
        u = queue.dequeue()
        # 搜索u的相邻节点
        for v in graph[u]:
            if v.color == Color.WHITE:
                v.color = Color.GRAY
                v.distance = u.distance + 1
                v.parent = u
                queue.enqueue(v)
        u.color = Color.BLACK


def print_path(graph, s, v):
    """
    打印图中源节点s到节点v的最短路径
    """
    if v == s:
        print(s.data)
    elif v.parent is None:
        print("no path from %s to %s exists" % (s.data, v.data))
    else:
        print_path(graph, s, v.parent)
        print(v.data)


class MyTestCase(unittest.TestCase):
    def test_bfs(self):
        n1 = Node("v")
        n2 = Node("r")
        n3 = Node("s")
        n4 = Node("w")
        n5 = Node("t")
        n6 = Node("x")
        n7 = Node("u")
        n8 = Node("y")

        graph = {
            n1: [n2],
            n2: [n1, n3],
            n3: [n2, n4],
            n4: [n3, n5, n6],
            n5: [n4, n6, n7],
            n6: [n4, n5, n7, n8],
            n7: [n5, n6, n8],
            n8: [n6, n7]
        }

        bfs(graph, n3)
        print_path(graph, n3, n8)
        self.assertEqual(2, n1.distance)
        self.assertEqual(1, n2.distance)
        self.assertEqual(0, n3.distance)
        self.assertEqual(3, n8.distance)


if __name__ == '__main__':
    unittest.main()
