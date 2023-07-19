def FactorsSet(array):
    c=1
    result_array=[]
    n=len(array)
    for i in range(1,(len(array)//2)+1):
        if n%i==0:
            c+=1
    
    print(c,*result_array,n)
array=list(map(int,input("enter the array: ").split()))
print(FactorsSet(array))