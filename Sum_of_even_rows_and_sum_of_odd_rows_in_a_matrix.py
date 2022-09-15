r,c=map(int,input().split())
mat=[]
for i in range(r):
    lst=list(map(int,input().split())) [:c]
    mat.append(lst)
ers=0
ors=0
for i in range(r):
    if i%2==0:
        ers=ers+sum(mat[i])
    else:
        ors=ors+sum(mat[i])
print(ers,ors)