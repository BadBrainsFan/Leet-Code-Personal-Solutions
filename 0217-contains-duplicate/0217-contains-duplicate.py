class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not Counter(nums) <= Counter(set(nums))