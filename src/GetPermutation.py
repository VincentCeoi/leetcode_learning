from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = []

        def dfs(current_depth, max_depth, path, list, is_used, start_index):
            if len(result) >= k:
                return

            if current_depth == max_depth + 1:
                result.append(path.copy())
                return

            for index in range(len(list)):
                if current_depth == 1 and index < start_index:
                    continue
                if is_used[index] is False:
                    path.append(list[index])
                    is_used[index] = True
                    dfs(current_depth + 1, max_depth, path, list, is_used, start_index)
                    is_used[index] = False
                    path.pop()
        list = []
        for n_index in range(n):
            list.append(n_index + 1)
        max_depth = n
        current_depth = 1
        path = []
        is_used = []
        for _ in range(n):
            is_used.append(False)
        total_size = 1

        for i in range(n - 1):
            total_size *= (i + 1)
        start_index = int(k / total_size) - 1
        for i in range(total_size * start_index):
            result.append([0])
        dfs(current_depth, max_depth, path, list, is_used, start_index)
        result_array = result[k - 1]

        result_string = ""
        for num in result_array:
            result_string += str(num)
        return result_string


n = 3
s = Solution()
#print(3 - (int(3 / 2) * (2 * 1) + 1))
#print(int(296662 / 40320))
s.getPermutation(3, 3)