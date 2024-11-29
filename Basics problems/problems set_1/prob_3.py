'''Given mark of student, Print the Grade
Grade A if mark is greater than or equal to 90
Grade B if mark is greater than or equal to 80
Grade C if mark if greater than or equal to 60
Grade D if mark if greer than or equal to 35
Fail if mark is lesser than 35
Input: 95
Expected Output:
Grade A
Explanation: Here 95 is greater than or equal to 90 so its Grade A'''

solution:

Mark=int(input("Enter:"))
if Mark >= 90 and Mark<=100:
    print("Grade A")
elif Mark >= 80 and Mark<90: 
    print("Grade B")
elif Mark >= 60 and Mark<80:
     print("Grade C")
elif Mark >=35 and Mark<60: 
     print("Grade D")
elif Mark>=0 and Mark<35: 
     print("FAIL")
else:
    print("Enter crt mark")
    
    
