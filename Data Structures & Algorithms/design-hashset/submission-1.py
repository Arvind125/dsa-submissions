class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    def __init__(self, val, next_node):
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

        if self.bucket[hk] is None:
            return
        
        curr = self.bucket[hk]
        
        # handle head node deletion
        if curr.val == key:
            self.bucket[hk] = curr.next
            return
        
        while curr and curr.next and curr.next.val != key:
            curr = curr.next
        
        if curr and curr.next:
            curr.next = curr.next.next
            return
            

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