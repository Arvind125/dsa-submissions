class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)

        mp = {}
        for x in nums:
            mp[x] = mp.get(x, 0) + 1
        
        buckets = [[] for _ in range(n+1)]
        for key, val in mp.items():
            buckets[val].append(key)
        
        ans = []
        for i in range(n, 0, -1):
            for key in buckets[i]:
                ans.append(key)

                if len(ans) == k:
                    break
            if len(ans) == k:
                break
        return ans

        