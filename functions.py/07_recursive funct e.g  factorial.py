def fact_recursive(num):
    if num==0 or num==1:
        return 1
    return num*fact_recursive(num-1)  # here funct calls it self, thats why due to this recursion it is called recursive function

print(fact_recursive(4))