r,c=map(int,input().split())
mat=[]
for i in range(r):
    lst=list(map(int,input().split())) [:c]
    mat.append(lst)
es=0
os=0
for i in range(r):
    for j in range(c):
        if mat[i][j]%2==0:
            es = es + mat[i][j]
        else:
            os = os + mat[i][j]
print(es,os)