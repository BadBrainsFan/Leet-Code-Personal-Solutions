class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        result = []
        nums.sort()

        for index, item in enumerate(nums):
            if item > 0:
                break

            if index > 0 and item == nums[index - 1]:
                continue

            left, right = index + 1, len(nums) - 1
            while left < right:
                threeSum = item + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([item, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                        
        return result