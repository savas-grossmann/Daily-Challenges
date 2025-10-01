# Leetcode 8 String to Integer

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) < 1:
            return 0
        sign = 1
        if s[0] == '+':
            s = s[1::]
        elif s[0] == '-':
            sign = -1
            s = s[1::]
        res = 0
        for x in s:
            if x.isdigit():
                res = res * 10 + int(x)
                if sign * res <= -2**31:
                    return -2**31
                elif sign * res >= 2**31 - 1:
                    return 2**31 - 1
            else:
                break
        return res * sign

sol = Solution()
print(sol.myAtoi("+1"))