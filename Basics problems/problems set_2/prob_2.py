'''Write a program to take x and print multiples of x till 1000.
Input:
100
Expected Output:
100
200
300
400
500
600
700
800
900
1000
Explanation - Input is 100, multiples of 100 is 100*1, 100*2, 100*3 and so on till 1000.'''

solution:

method_1:
x=100
#using while loop
count=1 #asign count=0
while count < x:
    print(count*x)
    count+=1
    if count==11:
        break
      
method_2:
x=100
#using for loop
for i in range(1,11):
    print(i*x)


    
