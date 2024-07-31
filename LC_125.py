# Leetcode 125 - https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        s = "".join([c for c in s if c.isalpha() or c.isalnum()]).lower()
        if s == s[::-1]:
            return True
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome("a"))