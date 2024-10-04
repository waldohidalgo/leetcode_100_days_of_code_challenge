class Node:
    def __init__(self,times,prev,next):
        self.words=set()
        self.times = times # veces en que ha aparecido cada palabra
        self.prev = prev
        self.next = next
    def __repr__(self):
        return f"Node({self.times},{self.words})"
class AllOne:
    def __init__(self):
        head = Node(0,None, None)
        tail=Node(float('inf'),None, None)
        self.head = head
        self.tail = tail
        head.next, tail.prev = tail, head
        head.prev, tail.next = tail, head
        self.hashmap_keys = {}

    def _create_next_node(self, prev_node, next_node,times,key):
        new_node = Node(times, prev_node, next_node)
        prev_node.next, next_node.prev = new_node, new_node
        new_node.words.add(key)
        return new_node
    
    def _delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key not in self.hashmap_keys:
            if self.head.next.times==1:
                self.head.next.words.add(key)
                self.hashmap_keys[key] = self.head.next
            else:
                new_node = self._create_next_node(self.head, self.head.next, 1,key)
                self.hashmap_keys[key] = new_node
        else:
            node = self.hashmap_keys[key]
            node.words.remove(key)
            if node.next.times == node.times + 1:
                if node.next == self.tail:
                    new_node = self._create_next_node(node, node.next, node.times + 1,key)
                    self.hashmap_keys[key] = new_node
                else:
                    node.next.words.add(key)
                    self.hashmap_keys[key] = node.next
            else:
                new_node = self._create_next_node(node, node.next, node.times + 1,key)
                self.hashmap_keys[key] = new_node

            if len(node.words) == 0:
                self._delete_node(node)

    def dec(self, key: str) -> None:
        # key existe 100% seguro
        node = self.hashmap_keys[key]
        node.words.remove(key)
        if node.times==1:
            del self.hashmap_keys[key]  
        elif node.prev.times == node.times - 1:
            if node.prev == self.head:
                new_node = self._create_next_node(node.prev, node, node.times - 1,key)
                self.hashmap_keys[key] = new_node
            else:
                node.prev.words.add(key)
                self.hashmap_keys[key] = node.prev
        else:
            new_node = self._create_next_node(node.prev, node, node.times - 1,key)
            self.hashmap_keys[key] = new_node

        if len(node.words) == 0:
                self._delete_node(node)

    def getMaxKey(self) -> str:
        prev_node=self.tail.prev
        if prev_node.times==0:
            return ""
        else:
            return next(iter(prev_node.words))

    def getMinKey(self) -> str:
        next_node=self.head.next
        if next_node.times==float('inf'):
            return ""
        else:
            return next(iter(next_node.words))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
allOne=AllOne()
allOne.inc("a")
allOne.inc("b")
allOne.dec("a")
allOne.inc("b")
allOne.inc("b")
allOne.inc("a")
allOne.dec("b")
allOne.dec("b")
allOne.inc("c")
allOne.inc("c")
allOne.inc("c")
allOne.inc("a")
allOne.inc("a")
print(allOne.head,allOne.head.next)
print(allOne.tail,allOne.tail.prev)
print(allOne.hashmap_keys)
# print(allOne.getMinKey())
# print(allOne.getMaxKey())
# print(allOne.getMinKey())
