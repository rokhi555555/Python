'''
problem2
write a prog to accept marks of 6 students and display them in ordered
list
'''
s1=input("enter marks of student 1: ")
s1=int(s1)
s2=input("enter marks of student 2: ")
s2=int(s2)
s3=input("enter marks of student 3: ")
s3=int(s3)
s4=input("enter marks of student 4: ")
s4=int(s4)
s5=input("enter marks of student 5: ")
s5=int(s5)
s6=input("enter marks of student 6: ")
s6=int(s6)
stdmarks=[s1,s2,s3,s4,s5,s6]
stdmarks.sort()
print(stdmarks)