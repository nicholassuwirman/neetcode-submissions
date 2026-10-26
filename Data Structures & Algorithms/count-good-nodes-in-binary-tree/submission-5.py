# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.biggest = root.val
        self.count = 0

        def dfs(root, biggest):
            if not root:
                return None

            if root.val >= biggest:
                biggest = root.val
                self.count += 1
            
            dfs(root.left, biggest)
            dfs(root.right, biggest)

            return biggest

        
        dfs(root, self.biggest)
        return self.count
            


