def merge(A,B):
    c=[]
    while(len(A)!=0 and len(B)!=0):
        if(A[0])<=B[0]:
            c.append(A.pop(0))
        else:
            c.append(B.pop(0))
    if(len(A)==0):
        c.extend(B)
    else :
        c.extend(A)
    
    return c

def mergeSort(elements):
    n = len(elements)
    if n==1:
        return elements
    m=int(n/2)
    A=mergeSort(elements[:m])
    B=mergeSort(elements[m:])
    C=merge(A,B)
    return C

def majEle(elements):
    count=1
    for i in range(len(elements)-1):
        if elements[i]==elements[i+1]:
            count+=1
        else:
            count=1
        if count>len(elements)/27:
            return 1
    return 0
         

def main():
    num_elements = int(input())
    elemets = [int(x) for x in input().split()]
    ele=mergeSort(elemets)
    print(majEle(ele))
main()