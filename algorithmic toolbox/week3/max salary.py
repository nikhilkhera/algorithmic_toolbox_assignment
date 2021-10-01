def check_order_greater(a,b):
    a=str(a)
    b=str(b)
    A=a+b
    B=b+a
    A=int(A)
    B=int(B)
    if(A>B):
        return a
    else:
        return b        
            

    

def maxsalary(num,n):
    
    final_num=""
    while(num):
        max=0
        for i in num :
            if (check_order_greater(i,max)==str(i)):
                max=i
        final_num = final_num+str(max)
        num.remove(max)
    return(final_num)
def main():
    n=int(input())
    list=[int(x) for x in input().split()]
    print(maxsalary(list,n))
main()
