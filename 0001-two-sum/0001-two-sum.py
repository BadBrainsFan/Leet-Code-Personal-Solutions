class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, item in enumerate(nums):
            value = target - item
            if value in hashmap:
                return [hashmap[value], index]
            hashmap[item] = index