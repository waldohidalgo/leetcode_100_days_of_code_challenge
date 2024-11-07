from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    
    def build_tree(self, arr):
        if not arr:
            return None
        
        
        root = TreeNode(arr[0])
        queue = deque([root])
        index = 1
        
        
        while queue and index < len(arr):
            node = queue.popleft()
            
            
            if arr[index] is not None:
                node.left = TreeNode(arr[index])
                queue.append(node.left)
            index += 1
            
            
            if index >= len(arr):
                break
            
            
            if arr[index] is not None:
                node.right = TreeNode(arr[index])
                queue.append(node.right)
            index += 1
        
        return root
    
    
    def print_tree(self,root):
        if not root:
            return "Empty Tree"
        
        queue = deque([root])
        result = []
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        
        
        while result and result[-1] is None:
            result.pop()
        
        return result
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val!=root2.val:
            return False
        return (
             self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right) 
             or 
             self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
        
bt=BinaryTree()        
#root1=bt.build_tree([1,2,3,4,5,6,None,None,None,7,8])
#root2=bt.build_tree([1,3,2,None,6,4,5,None,None,None,None,8,7])
root1=bt.build_tree([])
root2=bt.build_tree([1])
# print(bt.print_tree(root1))
# print(bt.print_tree(root2))

sol=Solution()
print(sol.flipEquiv(root1,root2))