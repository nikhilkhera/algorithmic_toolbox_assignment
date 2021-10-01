import math
import random
def median(data,n):
    if n%2 == 1:
        return data[n//2][0]
    else:
        i = n//2
        return (data[i - 1][0] + data[i][0])/2

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
    m=  n//2
    A=mergeSort(elements[:m],i)
    B=mergeSort(elements[m:],i)
    return merge(A,B,i)

def distance(A,B):
    return (((A[0] -B[0])**2) + ((A[1]-B[1])**2))**0.5

def checkmid(d,m,p1,p2):
    mergep1p2=merge(p1,p2,1)
    midarr=[]
    distmin=d
    do = 0
    for i in mergep1p2:
        if i[0]>=m-d or i[0]<=m+d:
            midarr.append(i)
    for i in range(len(midarr)):
        for j in range(1,8):
            if (i+j) <len(midarr):
                do = distance(midarr[i],midarr[i+j])
                if(do<distmin):
                    distmin=do
    return distmin,mergep1p2

def closestPair(P):
    n=len(P)
    if n<=1:
        return 9999999999,P
    if n==2:
        return distance(P[0],P[1]),sorted(P,key=lambda a:a[1])
    m=median(P,n)
    Left=[]
    Right=[]
    for i in P:
        if i[0]<m:
            Left.append(i)
        elif i[0]==m:
            if random.randint(0,1):
                Left.append(i)
            else:
                Right.append(i)
        else:
            Right.append(i)
    
    d1,p1 = closestPair(Left)
    d2,p2= closestPair(Right)
    d = min(d1,d2)
    d,mergp1p2=checkmid(d,m,p1,p2)
    return d,mergp1p2
'''
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
    d,_=closestPair(mergeSort(points,0))
    del _
    print(d) 

main()
'''

def test():
    
    while 1:
        points=[]
        #n=random.randint(2,10)
        n=3
        for i in range(n):
            points.append((random.randint(0,10),random.randint(0,10)))
        print(points)
        fast,_=closestPair(mergeSort(points,0))
        del _
        slow=slow_closestPair(points)
           
        if(fast!=slow):
            print("-----FAST:{}-----SLOW{}----".format(fast,slow))
            print("ERROR")
            break
        print("OK")
        del points

test()
'''
'''
def test2():
    points=[(1,1),(10,2),(1,0)]
    fast,_=closestPair(mergeSort(points,0))
    del _
    slow=slow_closestPair(points)
    if(fast!=slow):
        print("-----FAST:{}-----SLOW{}----".format(fast,slow))
        print("ERROR")
    else:
        print("OK")
test2()
'''