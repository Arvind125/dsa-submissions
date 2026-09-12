class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        mp = {}
        ans = 0
        for x in nums:
            if x not in mp:
                mp[x] = 0
            mp[x] += 1
            if mp[x] * 2 >= n:
                ans = x
                break
        
        return ans
        