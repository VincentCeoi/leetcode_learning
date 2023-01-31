from typing import List

# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请
#
# 你返回所有和为 0 且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。

# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。

# 深度遍历:
# deep, size, 遍历的list, 路径path, sum
# 先排序，如果sum 已经大于当前 target, 跳出
class Solution:

    # 暴力破解法
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def dfs(maxDeepth, list, path, currentDeepth, sum, target, index):
            if currentDeepth == maxDeepth:
                if sum == target:
                    result.append(path.copy())
                return
            if sum > target:
                return
            if index > len(list):
                return
            for currentIndex in range(index, len(list)):
                if currentIndex > index and list[currentIndex] == list[currentIndex - 1]:
                    continue
                path.append(list[currentIndex])
                sum += list[currentIndex]
                currentDeepth += 1
                dfs(maxDeepth, list, path, currentDeepth, sum, target, currentIndex + 1)
                currentDeepth -= 1
                sum -= list[currentIndex]
                path.pop()

        result = []
        path = []
        nums.sort()

        dfs(3, nums, path, 0, 0, 0, 0)

        return result
    # 双指针解法
    def doubelIndex(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()
        for first_index in range(len(nums)):

            if first_index > 0:
                if nums[first_index] == nums[first_index - 1]:
                    continue

            target = 0 - nums[first_index]
            left_index = first_index + 1
            right_index = len(nums) - 1

            while left_index < right_index:
                if left_index > first_index + 1:
                    if nums[left_index] == nums[left_index - 1]:
                        left_index += 1
                        continue
                if right_index < len(nums) - 1:
                    if nums[right_index] == nums[right_index + 1]:
                        right_index -= 1
                        continue
                if nums[left_index] > target:
                    break
                if nums[left_index] + nums[right_index] == target:
                    result.append([nums[first_index], nums[left_index], nums[right_index]])
                    left_index += 1
                elif nums[left_index] + nums[right_index] < target:
                    left_index += 1
                elif nums[left_index] + nums[right_index] > target:
                    right_index -= 1
        return result




deep = 0
size = 3
list = [0,0,0, 0]
s = Solution()
print(s.doubelIndex(list))


