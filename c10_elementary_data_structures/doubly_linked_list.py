# -*- coding: utf-8 -*-
"""
    双向循环链表
"""
import unittest


class Node(object):
    def __init__(self, key, next=None, prev=None):
        self.key = key
        self.next = next
        self.prev = prev


class DoublyLinkedList(object):

    def __init__(self):
        self.head = None

    def search(self, key):
        x = self.head
        while x is not None and x.key != key:
            x = x.next
        return x

    def insert(self, x):
        """
            将x插入到链表前端
        """
        x.next = self.head
        if self.head is not None:
            self.head.prev = x
        self.head = x
        x.prev = None

    def delete(self, x):
        if x.prev is not None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next is not None:
            x.next.prev = x.prev


class MyTestCase(unittest.TestCase):
    def test_doubly_linked_list(self):
        dll = DoublyLinkedList()
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
