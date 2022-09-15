n=int(input())
l=map(int,input().split())
x=set(l)
os=0
for i in x:
    if i%2==0:
        os=os+i
print(os)