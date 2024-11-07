from typing import Optional, List
from collections import deque

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
    def calculateDepths(self, root: Optional[TreeNode], depths: dict, level: int = 0) -> None:
        if not root:
            return
        
        depths[root.val] = level
        self.calculateDepths(root.left, depths, level + 1)
        self.calculateDepths(root.right, depths, level + 1)

    def calculateHeights(self, root: Optional[TreeNode], heights: dict) -> int:
        if not root:
            return -1
        
        left_height = self.calculateHeights(root.left, heights)
        right_height = self.calculateHeights(root.right, heights)
        
        heights[root.val] = 1 + max(left_height, right_height)
        return heights[root.val]
            
    def calculateMaxDepthsIfRemoved(self, root: Optional[TreeNode], heights: dict, depths: dict, maxDepthsIfRemoved: dict, currentMaxDepth: int = 0) -> None:
        if not root:
            return
        
        maxDepthsIfRemoved[root.val] = currentMaxDepth

        leftMaxDepth = max(currentMaxDepth, depths[root.val] + (heights[root.right.val]+1 if root.right else 0))
        rightMaxDepth = max(currentMaxDepth, depths[root.val] + (heights[root.left.val]+1 if root.left else 0))

        if root.left:
            self.calculateMaxDepthsIfRemoved(root.left, heights, depths, maxDepthsIfRemoved, leftMaxDepth)
        if root.right:
            self.calculateMaxDepthsIfRemoved(root.right, heights, depths, maxDepthsIfRemoved, rightMaxDepth)

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        heights = {}  
        depths = {}   
        maxDepthsIfRemoved = {}  

        self.calculateHeights(root, heights)
        self.calculateDepths(root, depths)
        self.calculateMaxDepthsIfRemoved(root, heights, depths, maxDepthsIfRemoved)

        return [maxDepthsIfRemoved[query] for query in queries]

    def printMaxDepthsIfRemoved(self,maxDepthsIfRemoved):
        for val, maxDepth in maxDepthsIfRemoved.items():
            print(f"Node(val={val},maxDepth={maxDepth})")
    def printHeights(self,heights):
        for val, height in heights.items():
            print(f"Node(val={val},height={height})")
    def printDepths(self,depths):
        for val, depth in depths.items():
            print(f"Node(val={val},depth={depth})")

    
bt=BinaryTree()
arr=[1,None,5,3,None,2,4]

root=bt.build_tree(arr)
print(bt.print_tree(root))


queries=[3,5,4,2,4]

sol=Solution()

print(sol.treeQueries(root,queries))