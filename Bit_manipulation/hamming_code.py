
n=input()
l=len(n)
p=0
for i in range(1,l):
    if (2**i >= i+l+1):
        p=i
        break
p=[0]+[ (2*i)-1 for i in range(1,p) ]
bits=[-1]*(len(p)+l)
j=0;i=0
while(j<len(p)+l):
    if j not in p:
        bits[j]=n[i]
        i+=1
    j+=1
lis=[list('0'*(len(p)-len(bin(i)[2:]))+bin(i)[2:]) for i in range(len(p)+l+1)]
s=list(zip(*lis))
s=(s[::-1])
print(s)
ans=[ [ bits[i-1] for i in range(len(a)) if a[i]=='1'][1:].count('1') for a in s ]
for i in range(len(ans)):
    if ans[i]%2==0:
        bits[p[i]]='0'
    else:
        bits[p[i]]='1'
print(bits)





    