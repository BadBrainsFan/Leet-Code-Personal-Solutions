class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        nums.sort()
        result = []
        for index, item in enumerate(nums):
            if item > target:
                break
            if index > 0 and item == nums[index -1]:
                continue
            left,right = index + 1, len(nums)-1
            while left < right:
                trio = item + nums[left] + nums[right]
                if trio > target:
                    right -= 1
                elif trio < target:
                    left += 1
                else:
                    result.append([item, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result