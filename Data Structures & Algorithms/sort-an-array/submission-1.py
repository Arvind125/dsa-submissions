# merge sort, quick sort, heap sort, timsort
class Solution:
    def partition(self, l, r, nums):
        pivot = nums[l]
        h = r
        i = l + 1

        while i <= h:
            if nums[i] >= pivot:
                nums[i], nums[h] = nums[h], nums[i]
                h -= 1
            else:
                i += 1

        nums[l], nums[h] = nums[h], nums[l]
        return h

    def quickSort(self, l, r, nums):
        if l >= r:
            return
        
        pi = self.partition(l, r, nums)

        # print(nums[l:r+1])
        self.quickSort(l, pi-1, nums)
        self.quickSort(pi+1, r, nums)


    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(0, len(nums) - 1, nums)
        return nums
