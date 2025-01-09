# Question : https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        non_zero_index = 0
        
        for i in range(n):
            if nums[i] != 0:
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
                non_zero_index += 1

solution = Solution()

nums = [0,1,0,3,12]
solution.moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

nums = [0, 0, 0, 0, 0]
solution.moveZeroes(nums)
print(nums)  # Output: [0, 0, 0, 0, 0]

