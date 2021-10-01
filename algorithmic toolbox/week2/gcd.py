def findgcd(a,b):
    if b==0:
        return a
    a1= a % b
    return findgcd(b,a1)

a,b=[int(x) for x in input().split()]
print(findgcd(a,b))