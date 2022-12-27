from typing import List

# [46] https://leetcode.cn/problems/permutations
# 深度优先算法
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                # 深拷贝
                copy_path = path.copy()
                res.append(copy_path)
                return

            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    # 深度遍历 并且不断添加后续的分支
                    dfs(nums, size, depth + 1, path, used, res)
                    # 以下两步回溯 use[i] 设成false 并且移除path , 做了什么就还原什么

                    used[i] = False
                    path.remove(nums[i])

        size = len(nums)
        if len(nums) == 0:
            return []

        used = [False for _ in range(size)]
        res = []
        dfs(nums, size, 0, [], used, res)
        return res


# new_array = [1]
list = [1, 2, 3]
s = Solution()
print(s.permute(nums=list))
# list.insert(6, 10)
# print(list)
#used = [False for _ in range(len(list))]
#print(used)
