#Question: https://leetcode.com/problems/two-sum/


#Solution 1:

class Solution:
    def twoSum(self, nums, target):
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

        return []  
solution = Solution()

nums1 = [2, 7, 11, 15]
target1 = 9
print(solution.twoSum(nums1, target1))  

nums2 = [3, 2, 4]
target2 = 6
print(solution.twoSum(nums2, target2))  

nums3 = [3, 3]
target3 = 6
print(solution.twoSum(nums3, target3))  