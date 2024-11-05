class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        hashmap = {}
        for index, item in enumerate(nums):
            value = target - item
            if value in hashmap:
                return [hashmap[value], index]
            else:
                hashmap[item] = index