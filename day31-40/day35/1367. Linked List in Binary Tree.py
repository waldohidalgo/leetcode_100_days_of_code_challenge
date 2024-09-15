from collections import deque
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def createTree(self, nums):
        if not nums:
            return None
        root = TreeNode(nums[0])
        nodes = deque([root])
        i = 1

        while i < len(nums):
            node = nodes.popleft()
            if nums[i] is not None:
                node.left = TreeNode(nums[i])
                nodes.append(node.left)
            i += 1
            if i < len(nums) and nums[i] is not None:
                node.right = TreeNode(nums[i])
                nodes.append(node.right)
            i += 1
        return root
    
    def createLinkedList(self, nums):
        if not nums:
            return None
        head = ListNode(nums[0])
        curr = head
        i=1
        while i < len(nums):
            curr.next = ListNode(nums[i])
            curr = curr.next
            i+=1
        return head

    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        if not head:
            return True
        if not root:
            return False
        def dfs(tree_node, head_node):
            if not head_node:
                return True
            if not tree_node:
                return False
            if tree_node.val != head_node.val:
                return False
            return dfs(tree_node.left, head_node.next) or dfs(tree_node.right, head_node.next)
        
        if dfs(root, head):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


sol=Solution()
head=sol.createLinkedList([1,4,2,6,8])
root=sol.createTree([1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3])
print(sol.isSubPath(head,root))