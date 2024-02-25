'''
write a prog to chek the given no is prime or not?
'''
no = int(input("enter any number : "))
prime =True
for i in range(2,no):
    if no%i==0:
        prime =False
        break
if prime :
  print("prime number")
else:
    print("Number  is not  Prime")

    