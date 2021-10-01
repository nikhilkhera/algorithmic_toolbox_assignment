def changemoney(n):
    curval =0
    coin=[10,5,1]
    i=0
    count=0
    while curval<n:
        while curval<n and (n-curval)>=coin[i]:
            curval = curval +coin[i]
            count=count+1
        i=i+1
    return count

def main():
    n= int(input())
    print(changemoney(n))

main()
         