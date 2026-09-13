# merge sort, quick sort, heap sort, timsort
class Solution:
    def mergeSortedArray(self, l, mid, r, nums):
        a = nums[l:mid+1]
        b = nums[mid+1: r+1]

        na, nb = len(a), len(b)
        i, j, k = 0, 0, l
        while i < na or j < nb:
            if i < na and j < nb:
                if a[i] < b[j]:
                    nums[k] = a[i]
                    i += 1
                else:
                    nums[k] = b[j]
                    j += 1
            elif i < na:
                nums[k] = a[i]
                i += 1
            else:
                nums[k] = b[j]
                j += 1
            
            k += 1


    def mergeSort(self, l, r, nums):
        if l >= r:
            return
        
        mid = l + (r- l)//2

        self.mergeSort(l, mid, nums)
        self.mergeSort(mid+1, r, nums)

        self.mergeSortedArray(l, mid, r, nums)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(0, len(nums) - 1, nums)
        return nums
        
        