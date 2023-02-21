from typing import List
# 剑指 Offer 04. 二维数组中的查找
# 在一个 n * m 的二维数组中，每一行都按照从左到右 非递减 的顺序排序，每一列都按照从上到下 非递减 的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
# 将二维数组当做一个 二叉树， 从右上角开始查询
class Solution:

    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:

        max_row = len(matrix)
        max_column = 0
        if max_row != 0:
            max_column = len(matrix[0]) - 1

            row = 0
            column = max_column

            while row < max_row and column >= 0:
                if target < matrix[row][column]:
                    column -= 1
                elif target > matrix[row][column]:
                    row += 1
                else:
                    return True

            return False

        else:
            return False

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
s = Solution()
print(s.findNumberIn2DArray(matrix, 13))