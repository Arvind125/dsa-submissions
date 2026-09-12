class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        a = nums.copy()

        for x in nums:
            a.append(x)
        return a