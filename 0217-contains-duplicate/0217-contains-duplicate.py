class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        duplicates = {}

        for num in nums:
            if num not in duplicates:
                duplicates[num] = 1
            else:
                return True
        return False