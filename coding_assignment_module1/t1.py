a=input("Enter integers:")
l=a.split(",")
for i in range(0,len(l)):
   l[i]=int(l[i])
print('list:',l)
t=tuple(l)
print('tuple:',t)
