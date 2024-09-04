# Definition for a binary tree node.

from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def _createTree(self, nums):
        if not nums:
            return None
        root = TreeNode(nums[0])
        nodes = [root]
        i = 1
        while i < len(nums):
            node = nodes.pop(0)
            if nums[i] is not None:
                node.left = TreeNode(nums[i])
                nodes.append(node.left)
            i += 1
            if i < len(nums) and nums[i] is not None:
                node.right = TreeNode(nums[i])
                nodes.append(node.right)
            i += 1
        return root
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        root=self._createTree(root)
        if root is None:
            return []
        stack=[]
        res=[]
        lastNode=None
        currentNode=root

        while stack or currentNode:
            if currentNode:
                stack.append(currentNode)
                currentNode=currentNode.left
            else:
                peekNode=stack[-1]
                if peekNode.right and lastNode!=peekNode.right:
                    currentNode=peekNode.right
                else:
                    res.append(peekNode.val)
                    lastNode=stack.pop()

        return res




    # def recorrerTraversal(self, root):
    
    #     def recorrer(root):
    #         if root:
    #             yield from recorrer(root.left)
    #             yield from recorrer(root.right)
    #             yield root.val
    #     return list(recorrer(root))
   

sol=Solution()


print(sol.postorderTraversal([1,2,3,4,5,None,6]))
