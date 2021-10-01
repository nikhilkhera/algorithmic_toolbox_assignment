def editDistance(s1,s2):
    n=len(s1)
    m=len(s2)
    D=[[0 for j in range (m)] for i in range (n)]
    for i in range(0,n):
        D[i][0]=i
    for j in range(0,m):
        D[0][j]=j
    for i in range(1,n):
        for j in range(1,m):
            '''mindist=9999999

            if D[i-1][j]+1<mindist:
                mindist=D[i-1][j]+1

            if D[i][j-1]+1<mindist:
                mindist=D[i][j-1]+1
                
            if s1[i]==s2[j]:
                if D[i-1][j-1]<mindist:
                    mindist=D[i-1][j-1]
            else:
                if D[i-1][j-1]+1<mindist:
                    mindist=D[i-1][j-1]+1

            D[i][j]=mindist
            '''
            insetion= D[i][j-1]+1
            deletion = D[i-1][j]+1
            match=D[i-1][j-1]
            mismatch=D[i-1][j-1]+1

            if s1[i]==s2[j]:
                D[i][j]=min(insetion,deletion,match)
            else:
                D[i][j]=min(insetion,deletion,mismatch)
    return D[-1][-1]
    


def main():
    s1=input()
    s2=input()
    empty="#"
    s1=empty+s1
    s2=empty+s2
    print(editDistance(s1,s2))

main()