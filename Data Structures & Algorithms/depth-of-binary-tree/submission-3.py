# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS recursive

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = 0
        q = deque([root])
        while q:
            # q is like a list, but you can pop from front too using popleft O(1)
            # It's just that access by index is O(n) compared to a list.
            # If you want to pop left at a list, then its O(n), as the rest needs to get shifted to the left
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:  # DO NOT USE ELIF
                    q.append(node.right)
            level += 1
        return level

        # if you use elif, on line 25, then the right child is only added when there is no left child

