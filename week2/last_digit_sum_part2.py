
import random
def fib_piasno(m):                                                      #to find the piasno period
    fiblist=[0,1]
    for i in range(2,m*m+1):
        fiblist.append(fiblist[i-1]+fiblist[i-2])
        if(fiblist[i]%m==1 and fiblist[i-1]%m==0 ):
            return (len(fiblist)-2)

def fib_sum_last_digit_for_complete_period(p):                           #to find the sum of last digits of a complete period
    fiblist=[0,1]
    sum=1
    for i in range (2,p):
        fiblist.append(fiblist[-1]+fiblist[-2]%10)
        sum=fiblist[-1]+sum
    return sum%10

def fib_sum(n):                                                             #to find the sum of last digits of a fibonacci no.
    equ = (n) % fib_piasno(10)
    if equ <= 1:
        return equ 
    the_complete_divisible_no = n-equ
    times = int(the_complete_divisible_no/n)  
    fiblist=[0,1]
    sum =1
    for i in range(equ-1):
        fiblist.append((fiblist[-1]+fiblist[-2])%10)
        sum=sum+fiblist[-1]
    return (sum%10 + (times*fib_sum_last_digit_for_complete_period(fib_piasno(10))%10))%10               
'''
def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    _sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10
'''


def main():
    n=int(input())
    print(fib_sum(n))

'''
def test():
    while(1):
        n= random.randint(1,10000)
        x= fib_sum(n)
        y=fibonacci_sum_naive(n)
        print(n)
        if x!=y:
            print("----FAST:",x,"----SLOW:",y,"----")
            print("-------worng-----")
            break
        print("ok")
test()
'''
main()