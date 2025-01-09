#  Question : https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0
        
        max_product = min_product = result = nums[0]
        
        for num in nums[1:]:
            temp_max = max(num, max_product * num, min_product * num)
            min_product = min(num, max_product * num, min_product * num)
            max_product = temp_max
            result = max(result, max_product)
        
        return result

solution = Solution()

nums = [2,3,-2,4]
print(solution.maxProduct(nums))  # Output: 6

nums = [-2,0,-1]
print(solution.maxProduct(nums))  # Output: 0

nums = [-2,3,-4]
print(solution.maxProduct(nums))  # Output: 24