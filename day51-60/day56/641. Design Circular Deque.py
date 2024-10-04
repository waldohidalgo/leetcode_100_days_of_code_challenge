class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularDeque:
    def __init__(self, k: int):
        self.max_size=k
        self.head = None
        self.tail = None
        self.size=0
    def __repr__(self) -> str:
        current=self.head
        output=[]
        while current and current!=self.tail:
            output.append(f'Node(current_val={current.val},prev_val={current.prev.val},next_val={current.next.val})')
            current=current.next

        if self.tail:
            output.append(f'Node(current_val={self.tail.val},prev_val={self.tail.prev.val},next_val={self.tail.next.val})')
        
        return str(output)
        
    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            if self.head is None:
                node=Node(value)
                self.head = node
                self.tail = node
                node.next = self.head
                node.prev = self.tail
            else:
                node = Node(value, self.tail,self.head)
                self.head.prev = node
                self.head = node
                self.tail.next = node
            self.size+=1
            return True
        else:
            return False
        
    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            if self.head is None:
                node=Node(value)
                self.head = node
                self.tail = node
                node.next = self.head
                node.prev = self.tail
            else:
                node = Node(value, self.tail,self.head)
                self.head.prev = node
                self.tail.next = node
                self.tail = node

            self.size+=1
            return True
        else:
            return False
        
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        elif self.size==1:
            self.head = None
            self.tail = None
            self.size-=1
            return True
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
            self.size-=1
            return True
        
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        elif self.size==1:
            self.head = None
            self.tail = None
            self.size-=1
            return True
        else:
            self.tail = self.tail.prev
            self.head.prev = self.tail
            self.tail.next = self.head
            self.size-=1
            return True
        
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.head.val
        
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.tail.val

    def isEmpty(self) -> bool:
        return self.size==0

    def isFull(self) -> bool:
        return self.size==self.max_size
    

# Your MyCircularDeque object will be instantiated and called as such:
myCircularDeque=MyCircularDeque(3)
print(myCircularDeque.insertLast(1))
print(myCircularDeque.insertLast(2))
print(myCircularDeque.insertFront(3))
print(myCircularDeque.insertFront(4))
print(myCircularDeque)
print(myCircularDeque.getRear())
print(myCircularDeque.isFull())
print(myCircularDeque.deleteLast())
print(myCircularDeque.insertFront(4))
print(myCircularDeque.getFront())
print(myCircularDeque)