def max(n1,n2,n3):
    if n1>n2:
        if n1>n3:
            return n1
        else:
            return n3
    else:
        if n2>n3:
            return n2
        else:
            return n3
num1 = int(input("Enter any number1 : "))
num2 = int(input("Enter any number2 : "))
num3 = int(input("Enter any number3 : "))
print(f"maximum of three numbers is : {max(num1,num2,num3)}")