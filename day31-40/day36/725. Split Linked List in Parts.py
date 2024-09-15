# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
    
        if length == 0:
            return [None] * k
    
        partSize = length // k
        remain = length % k
        
        parts = []
        curr = head
        
        for i in range(k):
            part_head = curr
            part_tail = curr
            
            current_part_size = partSize + (1 if i < remain else 0)
            
            for j in range(current_part_size - 1):
                if part_tail:
                    part_tail = part_tail.next
            
            if part_tail:
                next_part_head = part_tail.next
                part_tail.next = None
                curr = next_part_head
            
            parts.append(part_head)
        
        return parts
    
    def createList(self, nums):
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
        
                
        
sol=Solution()
head=sol.createList([1,2,3])
k=5
print(sol.splitListToParts(head,k))    
        
        

       