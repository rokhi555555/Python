'''
write a prog to print 8 unique(single) nos 

'''
#bc set is collection of unique nos having no repeation so we will use it 
A = set()
print(type(A))
a1 =int(input("Enter a no in set"))
a2 =int(input("Enter a no in set"))
a3 =int(input("Enter a no in set"))
a4 =int(input("Enter a no in set"))
a5 =int(input("Enter a no in set"))
a6 =int(input("Enter a no in set"))
a7 =int(input("Enter a no in set"))
a8 =int(input("Enter a no in set"))
# method 1
# A.add(a1)
# A.add(a2)
# A.add(a3)
# A.add(a4)
# A.add(a5)
# A.add(a6)
# A.add(a7)
# A.add(a8)

# print(A)
A ={a1,a2,a3,a4,a5,a6,a7,a8}
print(A)