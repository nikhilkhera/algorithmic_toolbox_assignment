def commonsubsequencethree(A,B,C):
    n=len(A)
    m=len(B)
    p=len(C)
    D=[[[0 for k in range(p)] for j in range(m)]for i in range(n)]
    
    '''for i in range(n):
        D[i][0]=0
    for j in range(m):
        D[0][j]=0
    '''
    for i in range(1,n):
        for j in range(1,m):
            for k in range(1,p):
                
                mismatch=D[i-1][j-1][k-1]
                match=D[i-1][j-1][k-1] +1

                if(A[i]==B[j]==C[k]):
                    D[i][j][k]=max(  D[i-1][j][k]  ,  D[i][j-1][k] ,  D[i][j][k-1] , D[i-1][j-1][k]  , D[i][j-1][k-1] , D[i-1][j][k-1],match)
                else:
                    D[i][j][k]=max(  D[i-1][j][k]  ,  D[i][j-1][k] ,  D[i][j][k-1] , D[i-1][j-1][k]  , D[i][j-1][k-1] , D[i-1][j][k-1],mismatch)

    return D[-1][-1][-1]
def main():
    n= int(input())
    A= [int(x)for x in input().split()]
    assert n == len(A)
    m= int(input())
    B= [int(x)for x in input().split()]
    assert m ==len(B)
    
    p= int(input())
    C= [int(x)for x in input().split()]
    assert p ==len(C)
    empty=[-9999999999]
    A=empty+A
    B=empty+B
    C=empty+C
    print(commonsubsequencethree(A,B,C))

main()