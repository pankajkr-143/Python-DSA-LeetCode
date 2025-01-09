# Question : https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums):
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
        
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

solution = Solution()

nums = [4,3,2,7,8,2,3,1]
print(solution.findDisappearedNumbers(nums))  # Output: [5, 6]

nums = [1, 1]
print(solution.findDisappearedNumbers(nums))  # Output: [2]

nums = [1, 1, 2, 2]
print(solution.findDisappearedNumbers(nums))  # Output: [3, 4]