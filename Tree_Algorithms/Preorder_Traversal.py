from typing import List
from Binary_Tree_ADT import *


def preorder(root: TreeNode) -> List[int]:
    """
    Traverse order: root, left, right
    """
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def make_tree() -> TreeNode:
    """
    Return a random list of n ints.
    """
    l2_1 = TreeNode(4)
    l2_2 = TreeNode(5)
    l2_3 = TreeNode(6)
    l2_4 = TreeNode(7)
    l1_1 = TreeNode(2)
    l1_1.left = l2_1
    l1_1.right = l2_2
    l1_2 = TreeNode(3)
    l1_2.left = l2_3
    l1_2.right = l2_4
    l0 = TreeNode(1)
    l0.left = l1_1
    l0.right = l1_2
    return l0


if __name__ == '__main__':
    root = make_tree()
    result = preorder(root)
    assert result == [1, 2, 4, 5, 3, 6, 7]
