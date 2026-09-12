class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        x = nums[0]
        cnt = 0
        for a in nums:
            if cnt == 0:
                x = a
                cnt = 1
            elif a == x:
                cnt += 1
            else:
                cnt -= 1
        return x
        