class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        fullBottles = numBottles
        remainingBottles = 0
        res = 0
        while True:
            res += fullBottles
            emptyBottles = fullBottles + remainingBottles
            if emptyBottles // numExchange < 1:
                break
            else:
                fullBottles = emptyBottles // numExchange
                remainingBottles = emptyBottles % numExchange
        return res

sol = Solution()
print(sol.numWaterBottles(15, 4))