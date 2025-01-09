# Question : https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

solution = Solution()

nums = [1,2,3,1]
print(solution.containsDuplicate(nums))  # Output: True

nums = [1,2,3,4]
print(solution.containsDuplicate(nums))  # Output: False

nums = [1,1,1,3,3,4,3,2,4,2]
print(solution.containsDuplicate(nums))  # Output: True