# 35 https://leetcode.cn/problems/search-insert-position/
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index in range(len(nums)):
            if target > nums[index]:
                continue
            else:
                return index
        return len(nums)

    # 使用二分法计算
    def searchByHalfSearch(self, nums: List[int], target: int) -> int:
        #count = 0
        middle = int (len(nums) / 2)
        index = 0
        if nums[middle] <= target:
            index = middle
        while index < len(nums):
            if target > nums[index]:
                index += 1
            else:
                return index
        return len(nums)


#middle = int(7 / 2)

#0,1,2,3,4,5,6

#print(middle)
list = [1,3,5,6]
s = Solution()
print(s.searchByHalfSearch(nums=list, target=2))
