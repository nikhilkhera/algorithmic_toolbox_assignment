def get_fibonacci_huge_naive(n):
    if n <= 1:
        return n

    prev2 = 0
    prev1  = 1
    sum=1
    current=0
    for _ in range((n-1)%60):
       current=(prev1%10+prev2%10)
       prev2=prev1
       prev1=current
       sum=current+sum
    return sum%10


inp = int(input())
print(get_fibonacci_huge_naive(inp))
