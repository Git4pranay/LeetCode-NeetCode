# Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

# Example 1:

# Input: a = 1, b = 2
# Output: 3
# Example 2:

# Input: a = 2, b = 3
# Output: 5

# My Method
# return sum([a,b])

#Method tht is correct
# we are going to xor the two binary rep and find carry by & oprtn repeat same until we get zero
# -> a=a^b , b=a&b<<1
a=int(input())
b=int(input())
while b!=0:
    c = a&b<<1
    a = a^b
    b = c
print(a)


