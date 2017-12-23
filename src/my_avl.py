

class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left_child = None
        self.right_child = None
        self.height = 1

    def balance_factor(self):
        if self.left_child is not None and self.right_child is not None:
            return self.right_child.height - self.left_child.height
        else:
            return 0

    def fix_height(self):
        if self.left_child is None or self.right_child is None:
            return

        left, right = self.left_child.height, self.right_child.height
        self.height = left + 1 if left > right else right + 1


class AVLTree:
    def __init__(self):
        "My tree will uppear here"


