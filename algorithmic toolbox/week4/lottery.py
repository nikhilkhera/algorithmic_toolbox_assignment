# Uses python3
import sys
import random

def merge(A,B):
    c=[]
    while(len(A)!=0 and len(B)!=0):
        if(A[0][0])<=B[0][0]:
            c.append(A.pop(0))
        else:
            c.append(B.pop(0))
    if(len(A)==0):
        c.extend(B)
    else :
        c.extend(A)
    
    return c

def mergeSort(elements):
    n=len(elements)
    if n==1:
        return elements
    m=int(n/2)

    A=mergeSort(elements[:m])
    B=mergeSort(elements[m:])
    return merge(A,B)
    


def fast_count_segments(starts, ends, points):
    count={}
    for i in points:
        count[i]=0
    
    #creating a new array consisting of points starts and ends values combined
    arr = []
    for i in range(len(starts)):                #the order has to be this while entering into the new array
        arr.append((starts[i],'l'))
    for i in points:
        arr.append((i,'p'))    
    for i in range(len(starts)):
        arr.append((ends[i],'r'))         
    newarr=mergeSort(arr)
    #counting the no. of segments
    stage=0
    i=0
    while i< (len(points)+(2*len(starts))):
        if newarr[i][1]=='l':
            stage+=1
        elif newarr[i][1]=='r':
            stage-=1
        else :
            count[newarr[i][0]]=stage
        i=i+1
    cnt=[]
    for i in points:
        cnt.append(count[i])
    return cnt
            

'''
def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt
'''
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    count=fast_count_segments(starts,ends,points)
    for i in count:
        print(i,end=' ')
    #use fast_count_segments
    #cnt = naive_count_segments(starts, ends, points)
    #for x in cnt:
    #    print(x, end=' ')
'''

def test():
    while 1:    
        points=[]
        for i in range(random.randint(1,50)):
            points.append(random.randint(0,10))

        segment_rng = random.randint(1,50)
        starts=[]
        ends=[0]*segment_rng
        for i in range(segment_rng):
            starts.append(random.randint(0,100))
            while ends[i]<=starts[i]:
                ends[i]=random.randint(0,150)
        print("POINTS:",points)
        print("SEGEMENT START:",starts)
        print("SEGMENT END:",ends)
        cnt1= fast_count_segments(starts,ends,points)
        cnt2= naive_count_segments(starts, ends, points)
        if cnt1!=cnt2:
            print("------SLOW:{}----FAST:{}----".format(cnt2,cnt1))
            print("-----ERROR-----")
            break
        print("ok")

test()
'''