class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mp = {}
        for x in nums:
            mp[x] = mp.get(x, 0) + 1
        
        a = list(mp.items())
        a.sort(key = lambda x: x[1])

        return [x[0] for x in a[-k:]]
        