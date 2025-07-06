class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n  # Initialize answer array with 1s

        # First pass: Calculate prefix products
        # answer[i] will store the product of all elements to the left of nums[i]
        prefix_product = 1
        for i in range(n):
            answer[i] = prefix_product
            prefix_product *= nums[i]

        # Second pass: Calculate suffix products and combine with prefix products
        # suffix_product will accumulate the product of elements to the right
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]
            
        return answer