# Question : https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            if left_sum == total_sum - left_sum - num:
                return i
            left_sum += num
        
        return -1
    
solution = Solution()

nums = [1,7,3,6,5,6]
print(solution.pivotIndex(nums))

nums = [1, 2, 3]
print(solution.pivotIndex(nums))

nums = [2, 1, -1]
print(solution.pivotIndex(nums))


