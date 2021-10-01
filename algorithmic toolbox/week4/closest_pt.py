import math
import statistics
import random

def distance(A,B):
    return math.sqrt(((A[0] -B[0])**2) + ((A[1]-B[1])**2))
    

def checkmid(d,P,m):
    midarr=[]
    distmin=d
    do = 0
    for i in P:
        if i[0]>=m-d or i[0]<=m+d:
            midarr.append(i)
    midarr.sort(key=lambda a: a[1])
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
    
    m=statistics.median(X)

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
        fast=closestPair(points)
        slow=slow_closestPair(points)
           
        if(fast!=slow):
            print("-----FAST:{}-----SLOW{}----".format(fast,slow))
            print("ERROR")
            break
        print("OK")
        del points
test()
'''