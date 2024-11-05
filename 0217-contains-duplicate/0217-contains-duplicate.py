class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = Counter(nums)
        for item in hashmap.values():
            if item != 1:
                return True
        return False