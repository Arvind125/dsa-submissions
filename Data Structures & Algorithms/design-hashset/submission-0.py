class MyHashSet:

    def __init__(self):
        self.dataset = [False] * 1000001
        
    def add(self, key: int) -> None:
        self.dataset[key] = True

    def remove(self, key: int) -> None:
        self.dataset[key] = False

    def contains(self, key: int) -> bool:
        return self.dataset[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)