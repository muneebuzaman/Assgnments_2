def sum_of_evens(n):
    sum=0
    even_numbers=[]
    for i in range(n+1):
        if i%2==0:
            sum+=i
    return sum
a=sum_of_evens(10)
b=sum_of_evens(20)
c=sum_of_evens(50)
print(a,'\n',b,'\n',c)
