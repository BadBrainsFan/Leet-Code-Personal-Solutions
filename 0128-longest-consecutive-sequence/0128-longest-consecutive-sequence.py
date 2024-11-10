class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSort = set(nums)
        longest = 0
        for n in nums:
            if (n - 1) not in numsSort:
                length = 0
                while (n + length) in numsSort:
                    length += 1
                longest = max(longest, length)
        return longest