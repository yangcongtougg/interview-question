# _*_ coding: utf-8 _*_
# @Time     :2018/3/13 12:33
# @Author   :maxzhangcong
# @Email    :maxzhangcong@163.com

"""
    *************模块文档注释**************
    二叉树的实现
    树节点的添加
"""


class Node(object):
    """节点类"""

    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None


class Tree(object):
    """树类"""

    def __init__(self):
        self.root_node = None

    def add(self, item):
        """
        添加节点
        :param item:
        :return:
        """

        node = Node(item)

        if self.root_node is None:
            self.root_node = node
            return

        queue = []
        queue.append(self.root_node)

        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        """
        广度遍历
        :return:
        """
        if self.root_node is None:
            return
        queue = []
        queue.append(self.root_node)

        while queue:
            cur_node = queue.pop(0)
            print(cur_node.item, end='')
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder_travel(self, root_node):
        """
        先序遍历 root>>>left>>>right
        :return:
        """
        if root_node is None:
            return
        print(root_node.item, end='')
        self.preorder_travel(root_node.lchild)
        self.preorder_travel(root_node.rchild)

    def inorder_travel(self, root_node):
        """
        中序遍历 left>>>root>>>right
        :param root_node:
        :return:
        """
        if root_node is None:
            return
        self.inorder_travel(root_node.lchild)
        print(root_node.item, end='')
        self.inorder_travel(root_node.rchild)

    def postorder_travel(self, root_node):
        """
        后序遍历 left>>>right>>>root
        :param root_node:
        :return:
        """
        if root_node is None:
            return
        self.postorder_travel(root_node.lchild)
        self.postorder_travel(root_node.rchild)
        print(root_node.item, end='')


if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.add(10)

    print('*' * 20 + '广度遍历' + '*' * 20)
    tree.breadth_travel()
    print('')
    print('*' * 20 + '先序遍历' + '*' * 20)
    tree.preorder_travel(tree.root_node)
    print('')
    print('*' * 20 + '中序遍历' + '*' * 20)
    tree.inorder_travel(tree.root_node)
    print('')
    print('*' * 20 + '后序遍历' + '*' * 20)
    tree.postorder_travel(tree.root_node)