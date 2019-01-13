import time


lst = []
spaces = []
a = -1

length = int(input("Enter the length of the list you want to introduce\n"))
print  ("Now input the data, and please press enter after each entry\n")
for i in range(length):
    lst.append(input())
    
start_time = time.time()

print("You have inputted the following list:\n",lst)
    

for i in range(length):
    if (lst[i]==' '):
        a=a+1
        spaces.append(i)

print("The minimum distance between the spaces is %s"%(spaces[1]-spaces[0]-1),"\n")
print("The maximum distance between the spaces is %s"%(spaces[a]-spaces[0]-1),"\n")
print("Time taken for the program to b executed is%s second"%(time.time()-start_time))