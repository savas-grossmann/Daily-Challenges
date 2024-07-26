# Leetcode 3 - https://leetcode.com/problems/longest-substring-without-repeating-characters
# https://www.geeksforgeeks.org/window-sliding-technique/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        substring = {}
        left, right = 0, 0
        maximum = 1
        while right < len(s):
            if s[right] in substring:
                left = max(left, substring[s[right]] + 1)
            maximum = max(maximum, right - left + 1)
            substring[s[right]] = right
            right += 1
            print(left, right, maximum)
        return maximum


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring("pwwkew"))
