# Question : https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums):
        current_sum = max_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum

solution = Solution()

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(solution.maxSubArray(nums))  # Output: 6

nums = [1]
print(solution.maxSubArray(nums))  # Output: 1

nums = [5,4,-1,7,8]
print(solution.maxSubArray(nums))  # Output: 23