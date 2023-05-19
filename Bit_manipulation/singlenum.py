# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1
# logic
# do xor of all elements
# 100
# 001
# 010
# 001
# 010
#  ->100 xor of above
# we will left out with which is unique
# work if duplicates are repated twice
l = list(map(int,input().split()))
x=0
for i in l:
   x=x^i 
print(x)
