# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

class Solution:
    def replaceSpace(self, s: str) -> str:
        result = ""
        for char in s:
            if char == " ":
                result += "%20"
            else:
                result += char
        return result

str = "we are not happy1"
s = Solution()
print(s.replaceSpace(str))