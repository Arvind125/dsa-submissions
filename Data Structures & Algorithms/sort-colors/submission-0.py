class Solution:
    def swap(self, i, j, nums):
        nums[i], nums[j] = nums[j], nums[i]

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        l = 0
        for i in range(n):
            if nums[i] == 0:
                self.swap(l, i, nums)
                l+=1
        
        for i in range(n):
            if nums[i] == 1:
                self.swap(l, i, nums)
                l += 1
        