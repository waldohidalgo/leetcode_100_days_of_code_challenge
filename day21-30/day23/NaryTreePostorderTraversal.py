from typing import List
#Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def createTree(self, nums):
        if not nums:
            return None
    
        root = Node(nums[0])
        queue = [root]
        
        i = 1
        while i < len(nums):
            if nums[i] is None:
                currentFather=queue.pop(0)
                i+=1
                while i<len(nums) and nums[i] is not None:
                    node=Node(nums[i])
                    currentFather.children.append(node)
                    queue.append(node)
                    i+=1          
        return root
    
    def postorderIterative(self, root: 'Node') -> List[int]:
        ## iterative to postorder traversal n-ary tree
        if root is None:
            return []
        else:
            stack = [root]
            result = []
            while stack:
                node = stack.pop()
                result.append(node.val)
                stack.extend(node.children) 
            return result[::-1]
        



    def postOrderRecursive(self,root: 'Node') -> List[int]:
        if root is None:
            return []
        else:
            res=[]
            for child in root.children:
                res+=self.postOrderRecursive(child)
            res.append(root.val)
            return res
                

sol=Solution()
root=sol.createTree([1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14])
print(sol.postorderIterative(root))
