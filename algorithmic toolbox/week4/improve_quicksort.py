# Uses python3
import sys
import random

def partition3(a,l,r):
    x=a[l]
    j1= l
    j2= l
    for i in range(l+1,r+1):
        if a[i]<x:
            a[i],a[j2+1] = a[j2+1],a[i]
            a[j1+1],a[j2+1]= a[j2+1],a[j1+1]
            j1+=1
            j2+=1
        else:
            if a[i]==x:
                a[i],a[j2+1]=a[j2+1],a[i]
                j2=j2+1
    a[l],a[j1] = a[j1],a[l]
    return j1,j2

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1,m2=partition3(a,l,r)
    #m = partition2(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)
'''    
def slow_randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition2(a, l, r)
    slow_randomized_quick_sort(a, l, m - 1)
    slow_randomized_quick_sort(a, m + 1, r)
'''
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
'''
def test():
    while(1):
        a=[]
        for i in range(random.randint(1,100)):
            a.append(random.randint(1,1000))
        print(a)
        b=list(a)
        randomized_quick_sort(a,0,len(a)-1)
        slow_randomized_quick_sort(b,0,len(b)-1)
        if(a!=b):
            print("-----fast: {} ---slow:{}----".format(a,b))
            print("------error-----")
            break;
        print("ok")
        del a

test()
'''