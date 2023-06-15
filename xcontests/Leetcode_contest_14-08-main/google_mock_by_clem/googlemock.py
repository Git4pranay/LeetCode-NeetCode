#two persons
l=[['9.00','10.30'],['12.00','13.00'],['16.00','18.00']] #list of time they were busy
t=['9.00','20.00'] # time for working
#person 2
l1=[['10.00','11.30'],['12.30','14.30'],['14.30','15.00'],['16.00','17.00']] 
t1=['10.00','18.30']
d=30 # the durination of meeting 
# STATEMENT is we have to find the meetings which possible for both p1 and p2 for d mins
def trans(s):
    p=list(s)
    s=int(s[:p.index('.')])*60+int(s[p.index('.')+1:])
    return s
def norm(t):
 ans=[];k=[]
 for i in range(trans(t[0]),trans(t[1])+1,30):
    ans+=[i//60,i%60]
 return ans
print(norm(t))
print(norm(t1))
ans1=[]
for i in l+l1:
    an1=[trans(i[0])//60,trans(i[0])%60]
    an=[trans(i[1])//60,trans(i[1])%60]
    ans1.append(an1)
    ans1.append(an1)
print(ans1)