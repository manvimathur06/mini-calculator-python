#Mini Calculator
while True:
    num1=float(input("enter the first number"))
    num2=float(input("enter the second number"))
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Floor Division")
    print("6.Power")
    print("7.Modulus")
    choice=int(input("enter the choice operation you want to perform"))
    match choice:
        case 1:
            print(num1 + num2)
    
        case 2:
             print(num1-num2)

        case 3:
            print(num1*num2)
        
        case 4:
            if num2==0:
                print("Zero is not allowed in Denominator")
            else:
                print(num1/num2)
        
        case 5:
            if num2==0:
                print("zero is not allowed in Denominator")
            else:
                print(num1//num2)
    
        case 6:
            print(num1**num2)
        
        case 7:
            if num2==0:
                print("zero is not allowed as Denominator")
            else:
                print(num1%num2)
            
        case _: 
            print("invalid choice")
        
    ans=input("Do You want to do perform calculation(Yes/No)")
    if ans.lower()!="yes":
        print("Thank-You")
        break
    
            
        
        
        
    