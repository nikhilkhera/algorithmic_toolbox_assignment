def merge(A,B,invA,invB):
    C=[]
    inv=invA+invB
    while len(A)!=0 and len(B)!=0:
        if(A[0]>B[0]):
            C.append(B.pop(0))
            inv+=len(A)
        elif A[0]==B[0]:
            C.append(A.pop(0))
        else:
            C.append(A.pop(0))
    if(len(A)==0):
        C.extend(B)
    else:
        C.extend(A)
        
    return C,inv


def mergeSort(elements):
    n=len(elements)
    if n<=1:
        return elements,0
    m=int(n/2)
    A,invA=mergeSort(elements[:m])
    B,invB=mergeSort(elements[m:])
    C,inv =merge(A,B,invA,invB)
    return C,inv

n= int(input())
elements=[int(x) for x in input().split()]
C,inv=mergeSort(elements)
print(inv)