class Solution:
    def swap(self, i, j, nums):
        nums[i], nums[j] = nums[j], nums[i]

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        l = 0
        r = n - 1
        i = 0
        while i <= r:
            if nums[i] == 0:
                self.swap(l, i, nums)
                l += 1
                i += 1
            elif nums[i] == 2:
                self.swap(r, i, nums)
                r -= 1
            else:
                i += 1

        