from typing import List


# [46] https://leetcode.cn/problems/permutations
# 深度优先算法
# 说明：
#
# 每一个结点表示了求解全排列问题的不同的阶段，这些阶段通过变量的「不同的值」体现，这些变量的不同的值，称之为「状态」； 使用深度优先遍历有「回头」的过程，在「回头」以后， 状态变量需要设置成为和先前一样
# ，因此在回到上一层结点的过程中，需要撤销上一次的选择，这个操作称之为「状态重置」；
# 深度优先遍历，借助系统栈空间，保存所需要的状态变量，在编码中只需要注意遍历到相应的结点的时候，状态变量的值是正确的，具体的做法是：往下走一层的时候，path
# 变量在尾部追加，而往回走的时候，需要撤销上一次的选择，也是在尾部操作，因此 path 变量是一个栈； 深度优先遍历通过「回溯」操作，实现了全局使用一份状态变量的效果。 使用编程的方法得到全排列，就是在这样的一个树形结构中完成
# 遍历，从树的根结点到叶子结点形成的路径就是其中一个全排列。
#
# 设计状态变量 首先这棵树除了根结点和叶子结点以外，每一个结点做的事情其实是一样的，即：在已经选择了一些数的前提下，在剩下的还没有选择的数中，依次选择一个数，这显然是一个 递归 结构； 递归的终止条件是： 一个排列中的数字已经选够了
# ，因此我们需要一个变量来表示当前程序递归到第几层，我们把这个变量叫做 depth，或者命名为 index ，表示当前要确定的是某个全排列中下标为 index 的那个数是多少； 布尔数组 used，初始化的时候都为 false
# 表示这些数还没有被选择，当我们选定一个数的时候，就将这个数组的相应位置设置为 true ，这样在考虑下一个位置的时候，就能够以 O(1)O(1)O(1) 的时间复杂度判断这个数是否被选择过，这是一种「以空间换时间」的思想。
# 这些变量称为「状态变量」，它们表示了在求解一个问题的时候所处的阶段。需要根据问题的场景设计合适的状态变量。

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # depth 深度，即一维数组的长度
        # 深度遍历的树状为depth 的深度
        # used 是有没有进行使用，即每个元素的排列顺序只能够出现一次 (路径不能重复)
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
# used = [False for _ in range(len(list))]
# print(used)
