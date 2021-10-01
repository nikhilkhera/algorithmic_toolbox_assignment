def minmakechange(n,coins):
    change=[0]
    for i in range(1,n+1):
        minchange=9999999
        for j in range(len(coins)):
            if coins[j]<=i:
                if change[i-coins[j]]+1<minchange:
                    minchange=change[i-coins[j]]+1
        change.append(minchange)   
    return change[n]


def main():
    n=int(input())
    coins=[1,3,4]
    print(minmakechange(n,coins))

main()