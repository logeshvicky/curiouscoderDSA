pattern 12:

n=4
for i in range(1,n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    for j in range(1,i+1-1):
        print("*",end=" ")
    print() 
for i in range(n+1-1):
    for j in range(1,i+1):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    for j in range(1,n-i):
        print("*",end=" ")      
    print()

output:

      *
    * * * 
  * * * * * 
* * * * * * * 
  * * * * * 
    * * * 
      * 
