class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize=maxSize
        self.head=None
        self.tail=None
        self.size=0
    def __repr__(self) -> str:
        current=self.head
        output=[]
        while current:
            output.append(current.val)
            current=current.next
        return str(output)

    def _is_full(self):
        return self.size==self.maxSize
    
    def _is_empty(self):
        return self.size==0
    def push(self, x: int) -> None:
        if self._is_full():
            return
        node=Node(x)
        if self._is_empty():
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            node.prev=self.tail
            self.tail=node
        self.size+=1
    def pop(self) -> int:
        if self._is_empty():
            return -1
        val=self.tail.val
        if self.size==1:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
        self.size-=1
        return val
    def increment(self, k: int, val: int) -> None:
        # increment the first k nodes by val their values
        current=self.head
        i=0
        while current and i<k:
            current.val+=val
            current=current.next
            i+=1
            


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

stk=CustomStack(3)
stk.push(1)
stk.push(2)
stk.pop()
stk.push(2)
stk.push(3)
stk.push(4)
print(stk)
stk.increment(5, 100)
stk.increment(2, 100)
print(stk)
print(stk.pop())
print(stk.pop())
print(stk.pop())
print(stk.pop())
print(stk)