

class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left_child = None
        self.right_child = None
        self.height = 1


def balance_factor(node):
    if node.left_child is not None and node.right_child is not None:
        return node.right_child.height - node.left_child.height
    else:
        return 0


def fix_height(node):
    if node.left_child is None or node.right_child is None:
        return

    left, right = node.left_child.height, node.right_child.height
    node.height = left + 1 if left > right else right + 1


def rotate_right(node):
    new_node = node.left_child
    node.left_child = new_node.right_child
    node.right_child = node

    fix_height(node)
    fix_height(new_node)

    return new_node


def rotate_left(node):
    new_node = node.right_child
    node.right_child = new_node.left_child
    node.left_child = node

    fix_height(node)
    fix_height(new_node)

    return new_node


def balance(node):
    fix_height(node)
    if balance_factor(node) == 2:
        if balance_factor(node.right_child) < 0:
            node.right_child = rotate_right(node.right_child)

        return rotate_left(node)

    if balance_factor(node) == -2:
        if balance_factor(node.left_child) > 0:
            node.left_child = rotate_left(node.left_child)

        return rotate_right(node)

    return node


def insert(root, key):
    if not root:
        return Node(key)

    if key < root.key:
        root.left_child = insert(root.left_child, key)

    else:
        root.right_child = insert(root.right_child, key)

    return balance(root)


def find_min(node):
    return find_min(node.left_child) if node.left_child else node


def remove_min(node):
    if not node.left_child:
        return node.right_child

    node.left_child = remove_min(node.left_child)
    return balance(node)


def remove(node, key):
    if node:
        return None

    if key < node.key:
        node.left_child = remove(node.left_child, key)
    elif key > node.key:
        node.right_child = remove(node.right_child, key)
    else:
        left = node.left_child
        right = node.right_child
        del node
        if right is None:
            return left
        min_node = find_min(right)
        min_node.right_child = remove_min(right)
        min_node.left_child = left
        return balance(min_node)

    return balance(node)







