# using for loop printing table for user given number
num =int(input("Enter any number: "))
for i in range(1,11):
   # print(str(num) + " X "+ str(i) + "= "+str(num*i))    # option 1
   print(f"{num} X {i} = {i*num}")          #fstrings  --> use: bc we can concatinat only strings so it provides ease 
   #f"{integers in curly braces} + {integer equations}+ strings}"