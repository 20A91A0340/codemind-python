a=int(input())
b=list(str(a))
c=set(b)
d=list(c)
if len(b)==len(d):
    print("Unique Number")
else:
    print("Not Unique Number")