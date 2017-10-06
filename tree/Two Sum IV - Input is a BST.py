# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import bisect


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        nums = self.get_nums(root)
        for i, num in enumerate(nums):
            j = bisect.bisect_left(nums, k - num)
            if i != j < len(nums) and nums[j] == k - num:
                return True
        return False

    def get_nums(self, node):
        if node:
            res = []
            res.extend(self.get_nums(node.left))
            res.append(node.val)
            res.extend(self.get_nums(node.right))
            return res
        return []
