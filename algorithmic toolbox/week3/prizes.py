def prize_dis(n):
    pr=[]
    i=1
    while n>0:
        if(n-i<=i):
            pr.append(n)
            break
        n=n-i
        pr.append(i)
        i=i+1

    return pr


def main():
    n=int(input())
    pr=prize_dis(n)
    print(len(pr))
    print(*pr)

main()