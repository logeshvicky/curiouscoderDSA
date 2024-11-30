'''Write a program to get firstName and lastName and n as input and print fullName that is firstName+lastName for n times.
Input
Nandy
Raja
5
Expected output:
NandyRaja
NandyRaja
NandyRaja
NandyRaja
NandyRaja
Explanation - Nandy is the firstName, Raja is the lastName and n is 5, so the expected output has NandyRaja printed 5 times'''

solution:

firstName=input("Enter:")
lastName=input("Enter:")
n=int(input("Enter:"))
for i in range(n):
    print(firstName+lastName)
