# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
#
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。


from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for each_list in matrix:
            size = len(each_list)
            # 二分法
            start_index = 0
            middle_index = int(size / 2)
            if each_list[middle_index] <= target:
                start_index += middle_index
            for start_index in range(0, size):
                if each_list[start_index] == target:
                    return True

        return False


test_list = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 20

s = Solution()
print(s.searchMatrix(matrix=test_list, target=20))
