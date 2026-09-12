class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        n = len(nums)

        i = n - 1
        while i >= 0:

            j = i
            while j >= 0 and nums[j] != val:
                j-=1
            
            if j < 0:
                break
            
            nums[i], nums[j] = nums[j], nums[i]
            i-=1
        k = i+1
        return k
        