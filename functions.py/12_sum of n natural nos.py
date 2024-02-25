def sumn(n):
    if n==1:
        return 1
    return n+ sumn(n-1)
n=int(input("Enter any number : "))
print(sumn(n))