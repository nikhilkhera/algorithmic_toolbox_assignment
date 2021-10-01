import random

'''
def maxpairwise(lis):
    result = 0
    for i in range(len(lis)):
        for j in range(len(lis)):
            if (lis[i]*lis[j] >result) and (i != j)  :
                result = lis[i]*lis[j]
    return result
'''
def fast_maxpairwise(lis):
    a= max(lis)
    lis.remove(a)
    b=max(lis)
    return a*b


def main():
    n=int(input())
    lis=[int(x) for x in input().split(" ",n-1)]
    result = fast_maxpairwise(lis)
    print(result)

'''
def main():
    while 1 :
        n=random.randint(2,100)
        print(n)
        lis=[]
        for x in range(n):
            lis.append(random.randint(1,1000))
        print(lis)
        fm=fast_maxpairwise(lis)
        m=maxpairwise(lis)
    
        if(fm!=m):
            print("fast value:",fm,"model",m)
            print("wrong")
            break
        else:
            print("ok")
'''
main()