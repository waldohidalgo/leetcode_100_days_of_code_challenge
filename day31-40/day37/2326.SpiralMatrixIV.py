# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        matrix=[[-1]*n for _ in range(m)]
        directions=[(0,1),(1,0),(0,-1),(-1,0)]

        i,j=0,0
        k=0
        curr=head
        isFull=False
        while m>0 and n>0 and not isFull:
            for r in range(n):
                if curr:
                    matrix[i][j]=curr.val
                    curr=curr.next
                else:
                    isFull=True
                if r==n-1:
                    k=(k+1)%4
                    m,n=m-abs(directions[k][0]),n-abs(directions[k][1])
                i,j=i+directions[k][0],j+directions[k][1]

            for r in range(m):
                if curr:
                    matrix[i][j]=curr.val
                    curr=curr.next
                else:
                    isFull=True
                if r==m-1:
                    k=(k+1)%4
                    m,n=m-abs(directions[k][0]),n-abs(directions[k][1])
                i,j=i+directions[k][0],j+directions[k][1]

        return matrix
    
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
head=sol.createList([0,1,2])

print(sol.spiralMatrix(1,4,head))