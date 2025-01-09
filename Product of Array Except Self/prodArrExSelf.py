# Question : https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n
        
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]
        
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        return answer

solution = Solution()

nums = [1, 2, 3, 4]
print(solution.productExceptSelf(nums))  # Output: [24, 12, 8, 6]

nums = [-1, 1, 0, -3, 3]
print(solution.productExceptSelf(nums))  # Output: [0, 0, 9, 0, 0]

nums = [1, 2, 3, 4, 5]
print(solution.productExceptSelf(nums))  # Output: [120, 60, 40, 30, 24]

