a,b=map(int,input().split())
lst1=[int(i) for i in input().split()]
lst2=list(map(int,input().split()))
s1=set(lst1)
s2=set(lst2)
s3=s1.intersection(s2)
print(len(s3))