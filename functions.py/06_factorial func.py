'''
factorial of no 5 is: 5!= 1*2*3...*5

n= 3
prod =1
for i in range(1,n):
  prod = prod*(i+1)
print(prod)
'''
def factorial(n):
    prod =1
    for i in range(1,n):
     prod = prod*(i+1)
    return prod


num = int(input("Enter any number "))
print(f"Factorial of no is : {factorial(num)}")