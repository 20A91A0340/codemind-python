r,c=map(int,input().split())
mat=[]
for i in range(r):
    lst=list(map(int,input().split())) [:c]
    mat.append(lst)
s=0
for i in range(r):
    for j in range(c):
        s = s + mat[i][j]
print(s)