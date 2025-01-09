# Question : https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-equal/

class Solution:
    def minimumOperations(self, nums):
        # Step 1: Create a set to store unique elements
        unique_elements = set()

        # Step 2: Count the number of operations needed
        operations = 0
        i = 0

        while i < len(nums):
            # Try adding the element to the set
            if nums[i] not in unique_elements:
                unique_elements.add(nums[i])
                i += 1
            else:
                # If an element is repeated, perform the operation
                operations += 1
                # Remove up to 3 elements from the beginning
                nums = nums[min(3, len(nums)):]
                i = 0  # Reset the index to start from the updated array
                unique_elements.clear()  # Reset the set to ensure distinct elements

        return operations

Solution = Solution()
nums = [1, 2, 3, 4, 2, 3, 3, 5, 7]
print(Solution.minimumOperations(nums))  # Output: 2

nums = [4,5,6,4,4]
print(Solution.minimumOperations(nums))  # Output: 1

nums = [6, 7, 8, 9]
print(Solution.minimumOperations(nums))  # Output: 0