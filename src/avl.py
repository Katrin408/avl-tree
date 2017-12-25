# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 02:26:42 2017

@author: Kate
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

    def fix_height(self):
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        self.height = 1 + max(left_height, right_height)

    def balance_factor(self):
        return (self.right.height if self.right else 0) - \
               (self.left.height if self.left else 0)

    def __repr__(self):
        return str(self.value)


class AVLTree:
    def __init__(self):
        self.node = None

    def add(self, value):
        self.node = self.insert(self.node, value)

    def to_list(self):
        node = self.node
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

    def collect(self):
        node = self.node
        collected = [[node]]
        while node:
            level = []
            for node in collected[-1]:
                if node is None:
                    return collected
                level.extend([node.left, node.right])

            collected.append(level)

    @staticmethod
    def node_dict(coordinates):
        return dict(
            xy=coordinates,
            xytext=coordinates,
            size=15,
            va="center",
            ha="center",
            bbox=dict(boxstyle="circle", fc="w"),
            arrowprops=dict(arrowstyle="-", fc="w")
        )

    def nodes_as_annotations(self):
        max_width = 100
        max_height = 90

        collected_tree = self.collect()
        new_tree = {}
        depth = len(collected_tree)
        width = len(collected_tree[-1])

        v_space = max_height / depth

        for i, level in enumerate(collected_tree):
            elements = len(level)
            node_h = v_space * (i + 1)
            h_space = max_width / (elements + 1)
            for j, node in enumerate(level):
                node_w = h_space * (j + 1)
                if node is not None:
                    new_tree[node] = AVLTree.node_dict((node_w / 100, 1 - node_h / 100))

        return new_tree

    def insert(self, root, value):
        if not root:
            return Node(value)
        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        return self.balance(root)

    @staticmethod
    def rotate_right(node):
        pivot = node.left
        node.left = pivot.right
        pivot.right = node
        node.fix_height()
        pivot.fix_height()
        return pivot

    @staticmethod
    def rotate_left(node):
        pivot = node.right
        node.right = pivot.left
        pivot.left = node
        node.fix_height()
        pivot.fix_height()
        return pivot

    def balance(self, node):
        node.fix_height()
        node_balance_factor = node.balance_factor()
        if node_balance_factor == 2:
            if node.right and (node.right.balance_factor() < 0):
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        if node_balance_factor == -2:
            if node.left and (node.left.balance_factor() > 0):
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        return node


if __name__ == "__main__":
    from drawtree import draw_bst
    tree = AVLTree()
    for i in range(16):
        tree.add(i)
    tree_ = [node.value for node in tree.to_list()]
    draw_bst(tree_)
    print(tree.collect())
