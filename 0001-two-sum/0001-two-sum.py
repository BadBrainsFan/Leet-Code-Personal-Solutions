class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for index, item in enumerate(nums):
            if target - item not in hashmap:
                hashmap[item] = index
            else:
                return [hashmap[target-item], index]