# -*- coding: utf-8 -*-
"""
    带哨兵的双向循环链表
"""
import unittest


class Node(object):
    def __init__(self, key, next=None, prev=None):
        self.key = key
        self.next = next
        self.prev = prev


class DoublyLinkedListSentinel(object):

    def __init__(self):
        self.nil = Node(None)
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def search(self, key):
        x = self.nil.next
        while x != self.nil and x.key != key:
            x = x.next
        return x if x != self.nil else None

    def insert(self, x):
        """
            将x插入到链表前端
        """
        x.next = self.nil.next
        self.nil.next.prev = x
        self.nil.next = x
        x.prev = self.nil

    def delete(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev


class MyTestCase(unittest.TestCase):
    def test_doubly_linked_list(self):
        dll = DoublyLinkedListSentinel()
        dll.insert(Node(1))
        x2 = Node(2)
        dll.insert(x2)
        dll.insert(Node(3))
        self.assertEqual(2, dll.search(2).key)
        self.assertEqual(1, dll.search(2).next.key)
        self.assertEqual(3, dll.search(2).prev.key)
        dll.delete(x2)
        self.assertIsNone(dll.search(2))


if __name__ == '__main__':
    unittest.main()
