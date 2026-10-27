# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        arr_nodes = []
        while q:
            arr_level = []
            for i in range(len(q)):
                node = q.popleft()
                arr_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            arr_nodes.append(arr_level)
        
        res = []

        for i in range(len(arr_nodes)):
            val = arr_nodes[i].pop()
            res.append(val)
        
        return res