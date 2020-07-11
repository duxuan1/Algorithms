from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    tree, stack = [], [root]
    while stack:
        node = stack.pop(0)
        tree.append(node.val)
        if node.right:
            stack.insert(0, node.right)
        if node.left:
            stack.insert(0, node.left)
    return tree


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
    result = dfs(root)
    print(result)
    assert result == [1, 2, 4, 5, 3, 6, 7]