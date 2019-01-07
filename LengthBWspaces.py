import time


s = input("enter a string here\n")
startime = time.time()

a=0
b=0
array = []
length = len(s)
for i in(s):
    if (i==' '):
        array.append(a)
        b=b+1
    a=a+1
print("Minimum distance between two spaces is ",array[1]-array[0]-1,"\n")
print("Maximum distance between two spaces is ",array[b-1]-array[0]-1,"\n")

print("Time taken by our program to complete is %s seconds"%(time.time() - startime))  
