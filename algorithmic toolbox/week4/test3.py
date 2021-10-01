import math
import random
def median(data):
    n = len(data)
    if n%2 == 1:
        return data[n//2]
    else:
        i = n//2
        return (data[i - 1] + data[i])/2

def merge(A,B,i):
    C=[]
    while(len(A)!=0 and len(B)!=0):
        if(A[0][i]<=B[0][i]):
            C.append(A.pop(0))
        else:
            C.append(B.pop(0))
    if len(A)==0:
        C.extend(B)
    else:
        C.extend(A)
    return C


def mergeSort(elements,i):
    n=len(elements)
    if n==1:
        return elements
    m=int(n/2)
    A=mergeSort(elements[:m],i)
    B=mergeSort(elements[m:],i)
    return merge(A,B,i)

def distance(A,B):
    return math.sqrt(((A[0] -B[0])**2) + ((A[1]-B[1])**2))

def checkmid(d,P,m):
    unsortedmidarr=[]
    distmin=d
    do = 0
    for i in P:
        if i[0]>=m-d or i[0]<=m+d:
            unsortedmidarr.append(i)
    midarr=mergeSort(unsortedmidarr,1)
    for i in range(len(midarr)):
        for j in range(1,8):
            if (i+j) <len(midarr):
                do = distance(midarr[i],midarr[i+j])
                if(do<distmin):
                    distmin=do
    return distmin

def closestPair(P):
    if len(P)<2:
        return 999999999999
    if len(P)==2:
        return distance(P[0],P[1])

    X=[]
    for i in P:
        X.append(i[0])
    
    m=median(X)
    
    Left=[]
    Right=[]
    for i in P:
        if i[0]<m:
            Left.append(i)
        elif i[0]==m:
            if(random.randint(0,1)):
                Left.append(i)
            else:
                Right.append(i)
        else:
            Right.append(i)
    
    d1 = closestPair(Left)
    d2= closestPair(Right)
    d = min(d1,d2)
    d=checkmid(d,P,m)
    return d

def slow_closestPair(P):
    distmin=999999999999
    do=0
    for i in range(len(P)):
        for j in range(i+1,len(P)):
            do=distance(P[i],P[j])
            if do<distmin:
                distmin=do
    return distmin
'''
def main():
    points=[]
    n=int(input())
    for i in range(n):
        points.append(tuple(int(x) for x in input().split()))
    d=closestPair(points)
    print(d) 

main()
'''
def test():
    while 1:
        points=[]
        n=random.randint(2,100)
        for i in range(n):
            points.append((random.randint(-100,100),random.randint(-100,100)))
        print(points)
        fast=closestPair(mergeSort(points,0))
        slow=slow_closestPair(points)
           
        if(fast!=slow):
            print("-----FAST:{}-----SLOW{}----".format(fast,slow))
            print("ERROR")
            break
        print("OK")
        del points
test()