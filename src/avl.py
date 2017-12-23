# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 02:26:42 2017

@author: Kate
"""

import random


class AVLTreeNode:
    u"Tree node"

    def __init__(self, value):
        self.setValue(value)
        self.setHeight(1)
        self.setLeft(None)
        self.setRight(None)

    def __str__(self):
        return str(self.value)

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height

    def fixHeight(self):
        leftHeight = self.left.getHeight() if self.left else 0
        rightHeight = self.right.getHeight() if self.right else 0
        self.setHeight(1 + max(leftHeight, rightHeight))

    def getBalanceFactor(self):
        return (self.right.getHeight() if self.right else 0) - \
               (self.left.getHeight() if self.left else 0)


class AVLTree:
    def __init__(self):
        self.node = None
        self.count = 0

    def add(self, value):
        self.node = self.__insertNode(self.node, value)

    def toList(self):
        return self.__toList(self.node)

    def toTreeList(self):
        return self.__toTreeList(self.node)

    def __toList(self, node):
        if not node:
            return None
        result = []
        if node.getLeft():
            result += self.__toList(node.getLeft())
        result += [node.getValue()]
        if node.getRight():
            result += self.__toList(node.getRight())
        return result

    def __toTreeList(self, node):
        if not node:
            return None
        result = []
        if node.getLeft():
            result.append(self.__toTreeList(node.getLeft()))
        result.append(node.getValue())
        if node.getRight():
            result.append(self.__toTreeList(node.getRight()))
        return result

    def __insertNode(self, root, value):
        if not root:
            return AVLTreeNode(value)
        if (value < root.getValue()):
            root.setLeft(self.__insertNode(root.getLeft(), value))
        else:
            root.setRight(self.__insertNode(root.getRight(), value))
        return self.__balance(root)

    def __rotateRight(self, node):
        pivot = node.getLeft()
        node.setLeft(pivot.getRight())
        pivot.setRight(node)
        node.fixHeight()
        pivot.fixHeight()
        return pivot

    def __rotateLeft(self, node):
        pivot = node.getRight()
        node.setRight(pivot.getLeft())
        pivot.setLeft(node)
        node.fixHeight()
        pivot.fixHeight()
        return pivot

    def __balance(self, node):
        node.fixHeight()
        nodeBalanceFactor = node.getBalanceFactor()
        if nodeBalanceFactor == 2:
            if node.getRight() and (node.getRight().getBalanceFactor() < 0):
                node.setRight(self.__rotateRight(node.getRight()))
            return self.__rotateLeft(node)
        if nodeBalanceFactor == -2:
            if node.getLeft() and (node.getLeft().getBalanceFactor() > 0):
                node.setLeft(self.__rotateLeft(node.getLeft()))
            return self.__rotateRight(node)
        return node

def traverse(root):
    current_level = [root]
    while current_level:
        print(' '.join(str(node) for node in current_level))
        next_level = []
        for n in current_level:
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
            current_level = next_level


def tree_to_list(node):
    tree = []

    def extract(node):
        if node:
            tree.append(node)
            if node.left:
                extract(node.left)
            if node.right:
                extract(node.right)
    extract(node)

    return tree


if __name__ == "__main__":
    tree = AVLTree()
    values = list(range(16))
    random.shuffle(values)

    for i in range(16):
        tree.add(values[i])

    tree = [node.value for node in tree_to_list(tree.node)]
    from drawtree import draw_bst
    draw_bst(tree)