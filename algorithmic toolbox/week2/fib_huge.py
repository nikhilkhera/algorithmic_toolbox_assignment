
import random
def fib_piasno(m):
    fiblist=[0,1]
    for i in range(2,m*m+1):
        fiblist.append(fiblist[i-1]+fiblist[i-2])
        if(fiblist[i]%m==1 and fiblist[i-1]%m==0 ):
            return (len(fiblist)-2)
def fib_remainder(n,m):
    equ = (n) % fib_piasno(m)
    if equ <= 1:
        return equ
    fiblist=[0,1]

    for i in range(equ-1):
        fiblist.append(fiblist[-1]+fiblist[-2])
    return fiblist[-1]%m

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current%m

'''
def main():
    n,m = [int(x) for x in input().split()]
    print(fib_remainder(n,m))

'''
def test():
    while(1):
        n= random.randint(1,10)
        m=random.randint(2,10)
        x= fib_remainder(n,m)
        y=get_fibonacci_huge_naive(n,m)
        print(n,m)
        if x!=y:
            print("----FAST:",x,"----SLOW:",y,"----")
            print("-------worng-----")
            break
        print("ok")
test()
#main()