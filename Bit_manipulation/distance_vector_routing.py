n = int(input('Enter no of nodes'))

rt=[[[0]*n,[0]*n] for i in range(n)] 
print(rt)

print('Enter cost matrix')
mat=[list(map(int,input().split())) for i in range(n)]

for i in range(n):
    for j in range(n):
        mat[i][i]=0;rt[i][0][j]=mat[i][j];rt[i][1][j]=j

print(rt)

for i in range(n):
    for j in range(n):
        for k in range(n):
            if rt[i][0][j] > mat[i][k] + rt[k][0][j] :
                rt[i][0][j] = rt[i][0][k] + rt[k][0][j]
                rt[i][1][j] = k
                
     
for i in range(n):
    print('router',i+1)
    for j in range(n):
        print("node",j+1,'via',rt[i][1][j]+1,"distance",rt[i][0][j])

