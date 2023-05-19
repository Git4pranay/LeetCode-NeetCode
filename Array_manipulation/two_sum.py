# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# check for 9 - x in left_list elements of the element
# x = 2,7,11,15

# dic = {} #left_list
# 9-2 = 7
# 7 is not in dic , add 2: index of 2
# dic = {2:0}
# 9-7 =2 
# 2 is in dic , return [ dic[2], index(7) ]

class Solution:
    def twoSum(self, nums, target) :
        dic = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in dic:
                return [dic[x],i]
            dic[nums[i]] = i

