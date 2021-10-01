def commonsubsequencetwo(A,B):
    n=len(A)
    m=len(B)
    D=[[0 for j in range(m)]for i in range(n)]
    '''for i in range(n):
        D[i][0]=0
    for j in range(m):
        D[0][j]=0
    '''
    for i in range(1,n):
        for j in range(1,m):

            insetion=D[i-1][j]
            deletion=D[i][j-1]
            mismatch=D[i-1][j-1]
            match=D[i-1][j-1]+1

            if(A[i]==B[j]):
                D[i][j]=max(insetion,deletion,match)
            else:
                D[i][j]=max(insetion,deletion,mismatch)
    return D[-1][-1]
def main():
    n= int(input())
    A= [int(x)for x in input().split()]
    assert n == len(A)
    m= int(input())
    B= [int(x)for x in input().split()]
    assert m ==len(B)
    empty=[-9999999999]
    A=empty+A
    B=empty+B
    print(commonsubsequencetwo(A,B))

main()