# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def createListNode(self, arr):
        head = ListNode(arr[0])
        curr = head
        for i in range(1, len(arr)):
            curr.next = ListNode(arr[i])
            curr = curr.next
        return head     
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        setNum=set(nums)
        curr=head
        newHead=None
        newCurr=None
        while curr:
            if curr.val in setNum:
                curr=curr.next
            else:
                if newHead is None:
                    newHead=ListNode(curr.val)
                    newCurr=newHead
                else:
                    newCurr.next=ListNode(curr.val)
                    newCurr=newCurr.next
                curr=curr.next
        return newHead

sol=Solution()

head=sol.createListNode([1,2,3,4])
#sol.showList(head)
sol.showList(sol.modifiedList([5],head))