from typing import List

# 思路: 统计需要 大小王 的张数， 以及总计大小王的张数，如果 两者相差大于1 的话，即false
# 如果有重复的非大小王扑克，直接返回false
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        count_not_asc = 0
        count_zero = 0
        for index in range(len(nums)):
            if nums[index] == 0:
                count_zero += 1
                continue
            if index != 0:
                if nums[index - 1] == 0:
                    continue;
                elif nums[index] - nums[index - 1] > 1:
                    #count_not_asc += 1
                    count_not_asc += (nums[index] - nums[index - 1])
                    continue
                elif nums[index] - nums[index - 1] == 0:
                    return False
        if count_not_asc - count_zero <= 1:
            return True
        else:
            return False
s = Solution();
print(s.isStraight([8,7,11,0,9]))


