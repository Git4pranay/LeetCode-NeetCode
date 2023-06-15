#if n==10 
# output:
# ----**    
# ---*--*   
# --*----*  
# -*------* 
# *--------*
# -*------* 
# --*----*  
# ---*--*   
# ----**    
# ---*--*
# --*----*
# -*------*
# *--------*
# -*------*
# --*----*
# ---*--*
# ----**
# ---*--*
# --*----*
# -*------*
# *--------*
# -*------*
# --*----*
# ---*--*
# ----**
# ---*--*
# --*----*
# -*------*
# *--------*
# -*------*
# --*----*
# ---*--*
# ----**
# ---*--*
# --*----*
# -*------*
# *--------*
# -*------*
# --*----*
# ---*--*
# ----**
# This can be done in any language c/c++/java
n=int(input())
m=n-n//2-1
g=n-m
p=g-2;q=g-1;ans=[]
for i in range(n//2):
  a=[]
  for j in range(g):
    if j==p or j==q:
        a.append("*")
    else:
     a.append('-')
  g+=1;p-=1;q+=1
  ans.append(''.join(a))
repeat=[]
for i in ans:
    repeat.append(i)
for i in range(n//2-2,-1,-1):
    repeat.append(ans[i])
for i in range(n//2):
    for j in repeat:
        print(j)
#In pure Python this is 4 lines of code :)
# n=int(input())
# l=[];x=n-2;y=0
# for i in range(n//2):
#     l.append("-"*y+"*"+"-"*x+"*")
#     x-=2;y+=1
# for i in range(n//2):
#     print(*(l[::-1]+l[1:]),sep="\n")


   