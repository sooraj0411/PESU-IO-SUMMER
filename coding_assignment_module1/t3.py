def sort(l):
    for i in range(0,len(l)):
        for j in range(0,len(l)-i-1):
            if(l[j]>l[j+1]):
                t=l[j]
                l[j]=l[j+1]
                l[j+1]=t
                
def binary(l,n):
    sort(l)
    ll=0
    ul=len(l)-1
    while ll<=ul:
        m=(ll+ul)//2
        if(l[m]<n):
            ll=m+1
        elif(l[m]>n):
            ul=m-1
        elif(l[m]==n):
            return 1
    return 0

li=[int(i) for i in input("Enter list:").split()]
n=int(input("Enter no:"))
c=binary(li,n)
if(c==0):
    print("Element not present")
else:
    print("Element present")

        
