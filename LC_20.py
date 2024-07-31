# Leetcode 20 - https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                queue.append(i)
            else:
                if queue:
                    if i == ')' and queue.pop() != "(":
                        return False
                    elif i == ']' and queue.pop() != "[":
                        return False
                    elif i == '}' and queue.pop() != "{":
                        return False
                else:
                    return False
        if len(queue) != 0:
            return False
        else:
            return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid("(]"))