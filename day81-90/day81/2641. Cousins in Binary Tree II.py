from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, arr):
        self.root = self.build_tree(arr)
    
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
    
    
    def print_tree(self):
        if not self.root:
            return "Empty Tree"
        
        queue = deque([self.root])
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
    
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        q = deque([root])
        root.val = 0  
        while q:
            level_sum = 0
            siblings_map = {}  
            
            for _ in range(len(q)):
                node = q.popleft()
                siblings_map[node] = (node.left, node.right)  
                if node.left:
                    level_sum += node.left.val
                    q.append(node.left)
                if node.right:
                    level_sum += node.right.val
                    q.append(node.right)
            
            
            for node, (left, right) in siblings_map.items():
                sibling_sum = 0
                if left:
                    sibling_sum += left.val
                if right:
                    sibling_sum += right.val
                
                if left:
                    left.val = level_sum - sibling_sum  
                if right:
                    right.val = level_sum - sibling_sum  
        
        return root
                

arr=[5,4,9,1,10,None,7]
bt=BinaryTree(arr)
root=bt.root        

print(bt.print_tree())

sol=Solution()
root=sol.replaceValueInTree2(root)
print(bt.print_tree())