class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mp = {}
        for x in nums:
            mp[x] = mp.get(x, 0) + 1
        
        a = [[val, key] for key, val in mp.items()]
        
        a.sort(reverse=True)

        return [x[1] for x in a[0:k]]
        