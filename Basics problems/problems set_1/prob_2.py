'''Write a program to check whether a triangle can be formed with the given values for the angles.
If sum of angles is equal to 180, then triangle can be formed, else it can't be formed.
Input: 45 45 45
Expected Output:
Triangle cannot be formed
Explanation -> We are getting 3 inputs, that is three angles of triangle, but here the sum of three angles 
that is 45+45+45 is not equal to 180 so Triangle cannot be formed is the output'''

solution:

#input from user
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=int(input("Enter the number:"))
d=a+b+c
if d==180: print("triangle can be formed")
else:print("triangle can't be formed")
