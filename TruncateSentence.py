# https://leetcode.com/problems/truncate-sentence/

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split(" ")
        return " ".join(words[:k])


# if __name__ == '__main__':
#    test = "Hello how are you Contestant"
#    k = 4
#    sol = Solution()
#    print(sol.truncateSentence(test, k))
