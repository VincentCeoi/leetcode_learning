from typing import List


# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串
# ""。
#
#
#
# 示例
# 1：
#
# 输入：strs = ["flower", "flow", "flight"]
# 输出："fl"
# 示例
# 2：
#
# 输入：strs = ["dog", "racecar", "car"]
# 输出：""
# 解释：输入不存在公共前缀。
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) > 0:
            compareStr = strs[0]
            result = 0
            for compareIndex in range(len(compareStr)):
                for i in range(len(strs)):
                    if (len(strs[i]) - 1 < compareIndex) or (compareStr[compareIndex] != strs[i][compareIndex]):
                        return compareStr[0:result]
                    if i == len(strs) - 1:
                        result = result + 1

            return compareStr[0:result]


s = Solution
a = ["cir", "car"]
#print(a[0][0:2])
print(s.longestCommonPrefix(s, strs=a))
#print(a[0][1])
