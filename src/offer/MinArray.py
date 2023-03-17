from typing import List

# 为什么是 low < high
# 为什么最后输出的是numbers[low] 而不是numbers[middle]
# 旋转数组查询最小

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        # 使用二分法
        low = 0
        high = len(numbers) - 1

        while low < high:
            middle = int((low + high) / 2)
            if numbers[middle] < numbers[high]:
                high = middle
            elif numbers[middle] > numbers[high]:
                low = middle + 1
            else:
                high -= 1
        return numbers[low]

        # 升序
        # if numbers[i] > numbers[i - 1]:
        #     while i < len(numbers):
        #         if numbers[i] < numbers[i - 1]:
        #             return numbers[i]
        #         else:
        #             i += 1
        # elif numbers[i] < numbers[i - 1]:
        #     while i > 0:
        #         if numbers[i] < numbers[i - 1]:
        #             return numbers[i]
        #         else:
        #             i -= 1
        # else:
        #     min = numbers[i]
        #     #先向后走， 遇到
        #     while i > 0:



        #while len(numbers) > i > 0:
            # 升序

        #def findAsc():

        #def findDesc():

        #return
s = Solution()
print(s.minArray([2,2,2,3,4,5,6,0,1]))