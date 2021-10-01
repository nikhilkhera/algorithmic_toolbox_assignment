def check_order_greater(a,b):
    small=min(a,b)
    small=str(small)
    big = max(a,b)
    big=str(big)
    a=str(a)
    b=str(b)
    length=min(len(a),len(b))
    for i in range(length):
        if int(a[i])>int(b[i]):
            return a
        if int(a[i])<int (b[i]):
            return b
        if i==length-1:
            if small[i]>(big)[i+1] :
                return small
            else: return big
            

    

def maxsalary(num,n):
    
    final_num=""
    while(num):
        max=0
        for i in num :
            if (check_order_greater(i,max)==str(i)):
                max=i
                print(max)
        final_num = final_num+str(max)
        num.remove(max)
    return(final_num)
def main():
    n=int(input())
    list=[int(x) for x in input().split()]
    print(maxsalary(list,n))
main()
