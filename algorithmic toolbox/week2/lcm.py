def findgcd(a,b):
    if b==0:
        return a
    a1= a % b
    return findgcd(b,a1)

def lcm(a,b):
    gcd=findgcd(a,b)
    a=a//gcd
    b=b//gcd
    return(a*gcd*b)

a,b=[int(x) for x in input().split()]
print(lcm(a,b))