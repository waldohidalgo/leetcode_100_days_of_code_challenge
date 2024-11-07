from typing import Optional
import heapq
from collections import deque

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
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        q = deque([root])
        min_heap = []
        
        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if len(min_heap) < k:
                heapq.heappush(min_heap, level_sum)
            else:
                if level_sum > min_heap[0]:
                    heapq.heapreplace(min_heap, level_sum)
        if k > len(min_heap):
            return -1
        return min_heap[0]






arr=[5,8,9,2,1,3,7]
bt=BinaryTree(arr)
root=bt.root
print(bt.print_tree())
print(Solution().kthLargestLevelSum(bt.root,4))