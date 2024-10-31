class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid_point = left + ((right - left) // 2)
            if nums[mid_point] > target:
                right = mid_point - 1
            elif nums[mid_point] < target:
                left = mid_point + 1
            else:
                return mid_point
        return -1