def primitivecalculator(n):
    if n==1:
        return [0,0]
    steps=[0,0]
    div=[2,3]
    for i in range(2,n+1):
        minstep=9999999
        if steps[i-1]+1<minstep:
            minstep=steps[i-1]+1
        for j in div:
            if i% j==0:
                if steps[i//j]+1<minstep:
                    minstep=steps[i//j]+1
        steps.append(minstep)
    return steps

def backtrack(steps,n):
    if n==1:
        return
    if n%2==0 and  steps[n]==steps[n//2]+1:
        backtrack(steps,n//2)
        print(n//2,end=" ")

    elif n%3==0 and  steps[n]==steps[n//3]+1:
        backtrack(steps,n//3)
        print(n//3,end=" ")
    else: 
        backtrack(steps,n-1)
        print (n-1,end=" ")
    return
    
def main():
    n=int(input())
    steps =primitivecalculator(n)
    print(steps[n])
    backtrack(steps,n)
    print(n)
main()