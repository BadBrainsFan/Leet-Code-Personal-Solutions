class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        duplicates = {}

        for index in range(len(nums)):
            if nums[index] not in duplicates.values():
                duplicates[nums[index]] = 1
            else:
                duplicates[nums[index]] += 1
        return len(duplicates.values()) != len(nums)
