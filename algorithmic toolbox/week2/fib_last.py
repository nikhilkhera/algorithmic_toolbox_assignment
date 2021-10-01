import re
n = int(input())
fiblist=[0,1]
fiblist.extend([-1]*n)
for i in range(2,n+1):
        fiblist[i]=fiblist[i-1]%m+fiblist[i-2]%m
print(fiblist[n])
