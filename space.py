def arraysum(a):
    sum=0
    for i in a:
        sum=sum+i
    return(sum)
a=[12,3,4,15]
print(arraysum(a))

def sum(n):
    return n*(n+1)/2
print(sum(10))

def summ(n):
    if (n<=0):
        return
    return n+summ(n-1)
