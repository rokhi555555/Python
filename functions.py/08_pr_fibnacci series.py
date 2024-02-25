'''
fibnacci series = 0,1,1,2,3,5,8,13,21,34,55,....
every no in series is sum of previous two terms
7th term= 6th + 5th terms


'''

def fibnacci_term(n):
    if n==0 or n==1:
        if n==0:
            return 0
        if n==1:
            return 1
    return fibnacci_term(n-2)+fibnacci_term(n-1)
number = int(input("Enter any no "))
print(fibnacci_term(number))