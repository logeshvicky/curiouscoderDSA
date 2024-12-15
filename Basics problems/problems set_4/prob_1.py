count of digit in number :

method_1:

n=987654321
count=0
while n>0:
    ld=n%10   #modulus operater will give last element
    count=count+1   
    n=n//10   #if we divide n with n it will remove last element
print(count)    

method_2:

n=987654321
print(int(len(str(n))))   #if we use int method n will back to intger
#print(len(str(n)))
