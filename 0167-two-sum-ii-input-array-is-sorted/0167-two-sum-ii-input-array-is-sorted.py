class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, item in enumerate(numbers):
            value = target - item
            if value in hashmap:
                return [hashmap[value] + 1, index + 1]
            hashmap[item] = index