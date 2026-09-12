class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class MyHashSet:
    def __init__(self):
        self.prime = 37
        self.bucket = [None] * self.prime
    
    def hashkey(self, key: int) -> int:
        return key % self.prime
        
    def add(self, key: int) -> None:
        if not self.contains(key):
            hk = self.hashkey(key)
            self.bucket[hk] = Node(key, self.bucket[hk])

    def remove(self, key: int) -> None:
        hk = self.hashkey(key)
        curr = self.bucket[hk]

        if curr is None:
            return

        # handle head node deletion
        if curr.val == key:
            self.bucket[hk] = curr.next
            return
        
        while curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        hk = self.hashkey(key)
        curr = self.bucket[hk]

        while curr:
            if curr.val == key:
                return True
            curr = curr.next
        return False
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)