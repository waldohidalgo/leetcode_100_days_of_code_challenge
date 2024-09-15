# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createList(nums):
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
class Solution(object):
    def findMCD(self,a,b):
        if a==b:
            return a
        elif a>b:
            residuo=a%b
            if residuo==0:
                return b
            else:
                return self.findMCD(b,residuo)
        else:
            residuo=b%a
            if residuo==0:
                return a
            else:
                return self.findMCD(a,residuo)
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr=head
        if not curr:
            return head
        while curr.next:
            MCD=self.findMCD(curr.val,curr.next.val)
            newNode=ListNode(MCD,curr.next)
            curr.next=newNode
            curr=curr.next.next
        return head
    
    def showList(self,head):
        curr=head
        while curr:
            print(curr.val)
            curr=curr.next
    
sol=Solution()
head=createList([7,789])
sol.showList(sol.insertGreatestCommonDivisors(head))