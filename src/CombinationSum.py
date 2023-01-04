# 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
#
# candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。
#
# 对于给定的输入，保证和为 target 的不同组合数少于 150 个。


from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 使用回溯算法 深度遍历
        result = []

        def deep_first_search(path, start_index, candidates, target):

            sum = 0
            for num in path:
                sum += num
            if sum > target:
                return
            elif sum == target:
                result.append(path.copy())
                return

# 关键点： 去除重复
            for index in range(start_index, len(candidates)):
                path.append(candidates[index])
                deep_first_search(path, index, candidates, target)
                # 判断是否大于 如果大于target 则retu在rn
                path.pop()

        # 排序
        candidates.sort()
        is_used = list()
        for i in range(len(candidates)):
            # is_used[i] = False
            is_used.append(False)
        start_index = 0
        path = []
        deep_first_search(path, start_index, candidates, target)
        return result


test = [2, 3, 6, 7]
s = Solution()
print(s.combinationSum(candidates=test, target=7))
