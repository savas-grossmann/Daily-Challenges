# https://leetcode.com/problems/reverse-string/

def reverseString(s):
    for i in range(int(len(s) / 2)):
        s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
    return s


if __name__ == '__main__':
    word = ["h", "a", "l", "l", "o"]
    print(word)
    print(reverseString(word))
