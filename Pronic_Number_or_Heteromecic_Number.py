import math
n=int(input())
m=int(math.sqrt(n))
if m*(m+1)==n:
    print("YES")
else:
    print("NO")