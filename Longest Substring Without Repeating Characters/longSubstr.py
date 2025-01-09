# Question : https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s):
        char_index = {}
        max_length = 0
        start = 0
        
        for i, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            char_index[char] = i
            max_length = max(max_length, i - start + 1)
        
        return max_length

solution = Solution()

s = "abcabcbb"
print(solution.lengthOfLongestSubstring(s))  # Output: 3

s = "bbbbb"
print(solution.lengthOfLongestSubstring(s))  # Output: 1

s = "pwwkew"
print(solution.lengthOfLongestSubstring(s))  # Output: 3