# -*- coding: utf-8 -*-
"""
    二叉搜索树
"""
import unittest


class Node(object):
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class BinarySearchTree(object):

    def __init__(self, root=None):
        self.root = root

    def insert(self, z):
        """
            插入节点z
        """
        # 保持遍历指针y作为x的双亲
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            # 树是空树
            self.root = y
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def search(self, x, key):
        """
            查找以x为根节点的树中关键字key的节点
        """
        if x is None or key == x.key:
            return x
        if key < x.key:
            return self.search(x.left, key)
        return self.search(x.right, key)

    def iterative_search(self, x, key):
        """
            查找以x为根节点的树中关键字key的节点
            非递归版本
        """
        while x is not None and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def transplant(self, u, v):
        """
            用v的子树替换u的子树
        """
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def delete(self, z):
        """
            删除z节点
        """
        if z.left is None:
            # 待删除节点z没有左孩子
            self.transplant(z, z.right)
        elif z.right is None:
            # 待删除节点z没有右孩子
            self.transplant(z, z.left)
        else:
            # y是z.right的最左节点
            y = self.minimum(x=z.right)
            if y.parent != z:
                # z的后继y不是z的右孩子
                # 先将z的右孩子链接为y的右孩子
                self.transplant(y, y.right)
                y.right = z.right
                z.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            z.left.parent = y

    def maximum(self, x=None):
        """
            返回x为根的树的关键字最大的元素
        """
        x = self.root if x is None else x
        while x.right is not None:
            x = x.right
        return x

    def minimum(self, x=None):
        """
            返回x为根的树的关键字最小的元素
        """
        x = self.root if x is None else x
        while x.left is not None:
            x = x.left
        return x

    def successor(self, x):
        """
            返回x的中序遍历后继元素
        """
        if x.right is not None:
            # x右子树非空，x的后继为x右子树中最左节点
            return self.minimum(x=x.right)
        # x右子树为空并且存在后继y，那么y是x的有左孩子的最低层祖先，
        # 并且y的左孩子也是x的一个祖先
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self, x):
        """
            返回x的中序遍历后继元素
        """
        if x.right is not None:
            # x左子树非空，x的前驱为x左子树中最左节点
            return self.maximum(x=x.left)
        # x左子树为空并且存在后继y，那么y是x的有右孩子的最低层祖先，
        # 并且y的右孩子也是x的一个祖先
        y = x.parent
        while y is not None and x == y.left:
            x = y
            y = y.parent
        return y


class MyTestCase(unittest.TestCase):
    def test_bst_opt(self):
        bst = BinarySearchTree(Node(0))
        self.assertEqual(0, bst.minimum().key)
        self.assertEqual(0, bst.maximum().key)
        bst.insert(Node(8))
        bst.insert(Node(3))
        bst.insert(Node(5))
        self.assertEqual(5, bst.search(bst.root, 5).key)
        self.assertEqual(5, bst.iterative_search(bst.root, 5).key)
        bst.insert(Node(2))
        bst.insert(Node(7))
        bst.delete(bst.search(bst.root, 5))
        self.assertIsNone(bst.search(bst.root, 5))
        bst.insert(Node(4))
        self.assertEqual(4, bst.successor(bst.search(bst.root, 3)).key)
        self.assertEqual(2, bst.predecessor(bst.search(bst.root, 3)).key)


if __name__ == '__main__':
    unittest.main()
