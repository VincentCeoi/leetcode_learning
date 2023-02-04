# 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
#
# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
#
# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        def find_all_unable_cell(current_depth, max_depth, row):
            unable_cell = {}
            n = 0
            for column in range(current_depth, max_depth):
                n += 1
                target1 = row + n
                target2 = row - n
                if target1 <= max_depth:
                    #key = column + "x" + target1
                    unable_cell[f'{column}x{target1}'] = 1
                if target2 >= 0:
                    unable_cell[f'{column}x{target2}'] = 1
                unable_cell[f'{column}x{row}'] = 1
            return unable_cell

        def deep_first_search(maxDepth, currentDepth, shouldNotUseList, path):
            if currentDepth > maxDepth:
                return
            for index in range(0, n):
                key = f'{currentDepth - 1}x{index}'
                location = ""
                for i in range(maxDepth):
                    # is_used[i] = False
                    if index == i:
                        location += "Q"
                    else:
                        location += "."
                if key in shouldNotUseList:
                    continue
                else:
                    path.append(location)
                    if currentDepth == maxDepth:
                        result.append(path.copy())
                        path.pop()
                        continue
                    unable_list = find_all_unable_cell(currentDepth, maxDepth, index)
                    cpUnableList = shouldNotUseList.copy()
                    cpUnableList.update(unable_list)
                    deep_first_search(maxDepth, currentDepth + 1, cpUnableList, path)
                    path.pop()


        # maxDepth = n
        currentDepth = 1
        shouldNotUseList = {}
        path = []
        deep_first_search(n, currentDepth, shouldNotUseList, path)

        return len(result)


s = Solution()
n = 5
a = 5
#print(f'{n}x{a}')
print(s.solveNQueens(n))
