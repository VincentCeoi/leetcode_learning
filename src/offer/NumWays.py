from typing import List


# https://leetcode.cn/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/solutions/
# 青蛙跳台阶，用深度优先搜索，并且使用Memory ，记录已经走过的路
class Solution:

    def __init__(self):
        self.result = 0
        self.memory = {}

    def numWays(self, n: int):

        def dfs(sum, case, target):
            if sum == target:
                self.result += 1
                return
            if sum > target:
                return

            for i in case:
                sum += i

                if self.memory.get(target - sum) is not None:
                    self.result += self.memory.get(target - sum)
                else:
                    beforeResult = self.result
                    dfs(sum, case, target)
                    # 添加到memory , 记录剩余的阶梯会出现的可能性，减少重复次数
                    self.memory[target - sum] = self.result - beforeResult
                # 回溯
                sum -= i

        # 剩下的目标
        sum = 0
        # 目前的有两种台阶
        case = [1, 2]
        dfs(sum, case, n)
        # if self.result > 1000000007:
        #     return int(self.result % (1e9+7))
        # else:
        #     return self.result
        return self.result % 1000000007


n = 78
s = Solution()
print(s.numWays(n))
