class signup:
    def __init__(s): #init constructor pre defined function initiate the value s in a class
        print("*****************WELCOM TO AGS CINEMA TICKET *****************")
        print("*******************SIGN UP PAGE*********************")
        print("*******************************************************")
        s.n=input("Enter your name:") 
        s.ph=input("Enter your phone number:")
        if len(s.ph)==1: #decision making
            s.e=input("Enter your E-mail:")
            if s.e.endswith("@gmail.com"):#string manupulation
                s.__pw=input("Enter your password:")
                if len(s.__pw)==1:#private
                    s.cp=input("Enter your conform password:")
                    if s.__pw==s.cp: #Relational operator or comparision operator
                        print("Done")
                        print("*************SIGN UP SUCCESSFULLUY*********************")
                    else:
                        print("Wrong password")
                        return signup()#jumping statement
                else:
                    print("something Password")
                    return signup()
            else:
                print("something Missing")
                return signup()
        else:
             print("Invalid Phone number")
             return signup()
    
    def get_ee(s): #Enscapsulation 
        return s.__pw
    def set_ee(s,NP):
        s.__pw=NP

class signin(signup):
    def __init__(s):#self parameter
        super().__init__()
        print("*************************************************")
        print("*****************SIGN IN PAGE*********************")
        print("*************************************************")
        Email=input("Enter your Email:")
        if s.e==Email:
            password=input("Enter your Password:")
            if  s.get_ee()==password:
                print(" Signin Succcessfully")
            else:
                print("Incorrect password")
                CP=input("DO you want to change your password(yes/no):")
                if CP=="yes":
                    NP=input("Enter your New Password:")
                    s.set_ee(NP)#set is asign value
                    print("your New Password is:",s.get_ee())#getter is return the value
        else:
            return signin()
s=signin()

class agscinema():
    def __init__(s):
        
        print("*************************************************")
        print("*************WELCOME TO AGS CINEMAS TICKET**************")
        print("*************************************************")
        print(">>>>>>>TODAY RELEASING MOVIES ARE<<<<<<<")
        print("BRAHMASTRA\nCOBRA\nCAPTAIN")
        print(".....Enter 1 is Brahmastra\n.....Enter 2 is Cobra\n.....Enter 3 is Caption")
        while True:
            s.c=int(input("Enter the number:"))
            if s.c==1 or s.c ==2 or s.c==3:
                break
            else:
                print("This movie is not showing in Ags Cinemas")

class movies(agscinema):
    def __init__(s):
        super().__init__()
        
        import time as t #Time module
        while True: #looping statement
            
            if s.c==1:
                print("welcome to Brahmastra movie")
                n=t.gmtime()
                print("Date",n[2]);print("Month",n[1]);print("Year",n[0])#lambda  function single line statement
                print("show time\n>>>>10.00\n>>>>2.00\n>>>>9.00")
                show=int(input("Enter show time:"))
                if show==10 or show==9 or show==2:
                    print(" show Time")
                    time=input("enter am / pm:")
                    st=str(show)+time #Arithematic Operator
                    print("Your show time is :",st)
                    print("Available 100 Rupees and 200 rupees Ticket")
                    print(">>>>Enter 100 is 100 Rupees Ticket\n>>>>Enter 200 is 200 Rupess Ticket")
                    Ticket=int(input("Enter the rupees:"))
                    if Ticket==100 or Ticket==200:
                        Members=int(input("Enter the members:"))
                        TT=Ticket*Members
                        print("Food items")
                        print(">>>one_litre_Water_bottle=50\n>>>one_chicken_burger=200\n>>>coke_one_litre_bottle=100\n>>>pop_corn=100")
                        one_litre_Water_bottle=50
                        w=int(input("Enter the how many water bottle:"))
                        Tw=one_litre_Water_bottle*w
                        one_chicken_burger=200
                        c=int(input("Enter the how many burger:"))
                        Tc=one_chicken_burger*c
                        coke_one_litre_bottle=100
                        co=int(input("Enter the how many coke bottle:"))
                        Tco=coke_one_litre_bottle*co
                        pop_corn=100
                        p=int(input("Enter the how many pop corn:"))
                        TP=pop_corn*p
                        TOTAL=TT+Tw+Tc+Tco+TP
                        print("Your Total Amount is :",TOTAL)
                        print("SUCCESSFULLEY  APPLIED ")
                        print("THANK U")
                        break
                    else:
                        print(Ticket,"Amount Ticket is not available")
                else:
                    print(show,"is no show time")
                    
            elif s.c==2:
                print("welcome to cobra movie")
                n=t.gmtime()
                print("Date",n[2]);print("Month",n[1]);print("Year",n[0])
                print("show time\n>>>>10.00\n>>>>2.00\n>>>>9.00")
                show=int(input("Enter show time:"))
                if show==10 or show==9 or show==2:
                    print(" show Time")
                    time=input("enter am / pm:")
                    st=str(show)+time #Arithematic Operator
                    print("Your show time is :",st)
                    print("Available 100 Rupees and 200 rupees Ticket")
                    print(">>>>Enter 100 is 100 Rupees Ticket\n>>>>Enter 200 is 200 Rupess Ticket")
                    Ticket=int(input("Enter the rupees:"))
                    if Ticket==100 or Ticket==200:
                        Members=int(input("Enter the members:"))
                        TT=Ticket*Members
                        print("Food items")
                        one_litre_Water_bottle=50
                        w=int(input("Enter the how many water bottle:"))
                        Tw=one_litre_Water_bottle*w
                        one_chicken_burger=200
                        c=int(input("Enter the how many burger:"))
                        Tc=one_chicken_burger*c
                        coke_one_litre_bottle=100
                        co=int(input("Enter the how many coke bottle:"))
                        Tco=coke_one_litre_bottle*co
                        pop_corn=100
                        p=int(input("Enter the how many pop corn:"))
                        TP=pop_corn*p
                        TOTAL=TT+Tw+Tc+Tco+TP
                        print("Your Total Amount is :",TOTAL)
                        print("SUCCESSFULLEY  APPLIED")
                        print("THANK U")
                        break
                    else:
                        print(Ticket,"Amount Ticket is not available")
                else:
                    print(show,"is no show time")
            elif s.c==3:
                print("welcome to caption movie")
                n=t.gmtime()
                print("Date",n[2]);print("Month",n[1]);print("Year",n[0])#lambda  function single line statement
                print("show time\n>>>>10.00\n>>>>2.00\n>>>>9.00")
                show=int(input("Enter show time:"))
                if show==10 or show==9 or show==2:
                    print(" show Time")
                    time=input("enter am / pm:")
                    st=str(show)+time #Arithematic Operator
                    print("Your show time is :",st)
                    print("Available 100 Rupees and 200 rupees Ticket")
                    print(">>>>Enter 100 is 100 Rupees Ticket\n>>>>Enter 200 is 200 Rupess Ticket")
                    Ticket=int(input("Enter the rupees:"))
                    if Ticket==100 or Ticket==200:
                        Members=int(input("Enter the members:"))
                        TT=Ticket*Members
                        print("Food items")
                        print(">>one_litre_Water_bottle=50\n>>>one_chicken_burger=200\n>>>coke_one_litre_bottle=100\n>>>pop_corn=100")
                        one_litre_Water_bottle=50
                        w=int(input("Enter the how many water bottle:"))
                        Tw=one_litre_Water_bottle*w
                        one_chicken_burger=200
                        c=int(input("Enter the how many burger:"))
                        Tc=one_chicken_burger*c
                        coke_one_litre_bottle=100
                        co=int(input("Enter the how many coke bottle:"))
                        Tco=coke_one_litre_bottle*co
                        pop_corn=100
                        p=int(input("Enter the how many pop corn:"))
                        TP=pop_corn*p
                        TOTAL=TT+Tw+Tc+Tco+TP
                        print("Your Total Amount is :",TOTAL)
                        print("ENJOY YOUR SHOW")
                        print("SUCCESSFULLEY  APPLIED")
                        break
                    else:
                        print(Ticket,"Amount Ticket is not available")
                else:
                    print(show,"is no show time")
                    


obj=movies()




