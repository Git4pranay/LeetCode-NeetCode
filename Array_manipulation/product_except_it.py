Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
class Solution:
    def productExceptSelf(self, nums):
        n=len(nums)
        ans = []
        s=1
        for i in range(n):
            s=s*nums[i]
            ans+=[s]
        k=1
        for i in range(1,n):
            ans[n-i] = k*ans[n-i-1]
            k = k*nums[n-i]
        ans[0]=k
        return (ans)
#beats 58%