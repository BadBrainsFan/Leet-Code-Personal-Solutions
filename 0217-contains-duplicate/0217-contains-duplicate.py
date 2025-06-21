class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}
        for index, item in enumerate(nums):
            if item not in duplicates:
                duplicates[item] = 1
            else:
                return True
        return False