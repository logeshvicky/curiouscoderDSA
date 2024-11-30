'''Write a program which takes two values x and y.
Prints x for y number of times.
Input:
2
3
Expected Output
2
2
2
Explanation - 2 is x and 3 is y in the input. So 2 is printed 3 times on the output.'''

solution:

#method_1:
x=int(input("Enter:"))
y=int(input("Enter:"))
#using for loop
for _ in range(y):
    print(x)
  
#method_2:
x=int(input("Enter:"))
y=int(input("Enter:"))
#using while loop
count=0 #asign count=0
while count < y:
    print(x)
    count+=1
    

