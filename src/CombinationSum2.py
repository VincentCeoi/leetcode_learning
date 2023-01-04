# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用 一次 。
#
# 注意：解集不能包含重复的组合。


from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
                if index > start_index and candidates[index] == candidates[index - 1]:
                    continue
                path.append(candidates[index])
                deep_first_search(path, index + 1, candidates, target)
                # 判断是否大于 如果大于target 则return
                path.pop()

        # 排序
        candidates.sort()
        is_used = list()
        for i in range(len(candidates)):
            is_used.append(False)
        path = []
        deep_first_search(path, 0, candidates, target)
        return result


test = [2,5,2,1,2]
s = Solution()
print(s.combinationSum2(candidates=test, target=5))
