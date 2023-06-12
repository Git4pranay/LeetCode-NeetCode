# In the realm of the Super 30 batch, Raj, their esteemed mentor, introduced them to a mysterious array with a hidden secret.

# Raj unveiled the enigmatic challenge, "Given array  of size , containing only 1's, 2's, and 3's, and  queries where each query consists of two integers  and , can you determine the count of each number in array between indices  and ?"

# Note:  and  use 1-based indexing.

# Intrigued by the array's secrets, the Super 30 batch embarked on a quest to unravel its mysteries. Armed with their coding skills and a thirst for knowledge, they delved deep into the array, meticulously examining the elements between the specified indices. Through diligent analysis and precise calculations, they successfully determined the counts of each number within the given range.

# As they solved the queries, the Super 30 batch not only enhanced their array manipulation skills but also discovered the beauty of data analysis and the art of extracting valuable information from seemingly ordinary arrays. This adventure became a testament to their growth as coding enthusiasts and their ability to conquer any coding challenge that came their way.

# Input Format

# First line contains a single integer  denoting the number of testcases.

# In each test case, the first line contains two space separated integers denoting the values of  and  respectively.

# The second line contains  space separated integers representing the elements of the array.

# The next  line contans two space spearated integers representing  and .

# Constraints





# Note that the sum of  and  over all test cases will not exceed 

# Output Format

# For each query, print 3 space sparated integers representing the count of 1's, 2's and 3's in the given range.

# Sample Input 0

# 2
# 5 2
# 1 3 3 3 3
# 1 5
# 3 4
# 4 1
# 2 2 1 1
# 1 2
# Sample Output 0

# 1 0 4
# 0 0 2
# 0 2 0

t = int(input())

for i in range(t):
    s,n=map(int,input().split())
    li=list(map(int,input().split()))
    
    dp = [[0,0,0]]
    one=0;two=0;three=0
    for i in li:
        if i==1:
            one+=1
        elif i==2:
            two+=1
        else:
            three+=1
        dp += [[one,two,three]]
    for _ in range(n):
       l,r=map(int,input().split())
       print(dp[r][0]-dp[l-1][0],dp[r][1]-dp[l-1][1],dp[r][2]-dp[l-1][2])
    print(dp)