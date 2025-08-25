# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # [3],[9, 20], [15, 7] level order traversing
        # [[3],[19,20],[15,7]]
        # [15, 7],[9, 20], [3] level order traversing - ii

        if not root:
            return []

        queue = deque([root])
        result = deque()
        # result = []

        while queue:
            temporary = []

            for _ in range(len(queue)):
                node = queue.popleft()
                temporary.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.appendleft(temporary)
            # result.append(temporary)

        return list(result)
        # return result