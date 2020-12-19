# 3 solutions to Leetcode 1. two sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Solution 1:

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        # Solution 2:

        dic = {}
        for i, amount in enumerate(nums):
            dic[i] = amount
        for key1 in dic:
            for key2 in dic:
                if key1 < key2:
                    if dic[key1] + dic[key2] == target:
                        return [key1, key2]

        # Solution 3:

        table1 = dict()
        for (i, num) in enumerate(nums):
            num1 = target - num
            if num1 in table1:
                return [i, table1[num1]]
            else:
                table1[num] = i


sol1 = Solution()
print(sol1.twoSum([3, 2, 4], 6))
