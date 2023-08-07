a=str(input("Ehter student name:"))
b=str(input("Enter the DOB:"))
c=int(input("Enter the class:"))
s1=int(input("Enter the subeject 1 Mark:"))
if(s1>=35):
    print("Pass")
else:
    print("Fail")
s2=int(input("Enter the subeject 2 Mark:"))
if(s2>=35):
    print("Pass")
else:
    print("Fail")
s3=int(input("Enter the subeject 3 Mark:"))
if(s3>=35):
    print("Pass")
else:
    print("Fail")
s4=int(input("Enter the subeject 4 Mark:"))
if(s4>=35):
    print("Pass")
else:
    print("Fail")
s5=int(input("Enter the subeject 5 mark:"))
if(s5>=35):
    print("Pass")
else:
    print("Fail")
TM=s1+s2+s3+s4+s5
print(TM)
if(TM>450 and TM<500):
    print("Grade is O")
    print("Excellent")
elif(TM<450 and TM>400):
    print("Grade is A")
    print("Very Good")
elif(TM<400 and TM>350):
     print("Grade is A+")
     print("Good")
elif(TM<350 and TM>300):
     print("Grade is B")
     print("Try well")
elif(TM<300 and TM>250):
     print("Grade is b+")
     print("Very Bad")
elif(TM<250):
    print("Grade is U")
    print("Poor")
    
