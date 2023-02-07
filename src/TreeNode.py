# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # def __int__(self, nums: List[int]):
    #    for i in nums:
    def createTreeFromList(self, root_index, nums=List[int]):
        if root_index >= len(nums):
            return None
        rootNode = TreeNode()
        rootNode.setValue(nums[root_index])
        rootNode.setLeft(self.createTreeFromList(2 * root_index + 1, nums))
        rootNode.setRight(self.createTreeFromList(2 * root_index + 2, nums))
        return rootNode

    def __int__(self):
        self.val = None
        self.left = None
        self.right = None

    def setValue(self, value=None):
        self.val = value

    def setLeft(self, left=None):
        self.left = left

    def setRight(self, right=None):
        self.right = right

    def pre_order_traversal(self, root):
        if root is not None:
            print(root.val)
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)


t = TreeNode()
a = t.createTreeFromList(0, [1, 2, 5, 3, 4, None, 6])
a.pre_order_traversal(a)
