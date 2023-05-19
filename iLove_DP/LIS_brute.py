Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?


# My code wont work for list all having same values means its not strcitly increasing 


# X = list(map(int,input().split()))
# Y=sorted(X)
# n=m=len(X)


# DP = [[None]*(n+1) for i in range(m+1)]
# for i in range(m+1):
#         for j in range(n+1):
#             if i == 0 or j == 0 :
#                 DP[i][j] = 0
#             elif X[i-1] == Y[j-1]:
#                 DP[i][j] = DP[i-1][j-1]+1
#             else:
#                 DP[i][j] = max(DP[i-1][j] , DP[i][j-1])
# print(DP[m][n])
 