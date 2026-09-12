class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        mp = {}
        ans = []
        for i in range(n):
            rem = target - nums[i]
            if rem in mp:
                ans = [mp[rem], i]
                break
            
            mp[nums[i]] = i
        return ans
        
        