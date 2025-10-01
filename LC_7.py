# Leetcode 7 reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        sign = ""
        if x[0] == "-":
            sign = "-"
            x = x[1:]
        res = int(sign + x[::-1])
        if res <= -2**31 or res > (2**31) - 1:
            return 0
        return res

sol = Solution()
print(sol.reverse(1534236469))
