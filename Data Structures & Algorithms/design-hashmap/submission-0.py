class Node:
    def __init__(self, key, value, next_node=None):
        self.key = key
        self.value = value
        self.next = next_node

class MyHashMap:

    def __init__(self):
        self.prime = 37
        self.bucket = [None] * self.prime
    
    def hashkey(self, key) -> int:
        return key % self.prime

    def put(self, key: int, value: int) -> None:
        hk = self.hashkey(key)
        curr = self.bucket[hk]

        # update if already exists
        while curr:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next
        # insert new
        self.bucket[hk] = Node(key, value, self.bucket[hk])
        

    def get(self, key: int) -> int:
        hk = self.hashkey(key)
        curr = self.bucket[hk]

        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1
        

    def remove(self, key: int) -> None:
        hk = self.hashkey(key)
        curr = self.bucket[hk]

        if curr is None:
            return
        if curr.key == key:
            self.bucket[hk] = curr.next

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)