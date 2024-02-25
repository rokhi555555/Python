def printTable(n):
  for i in range(1,11):
    print(f"{i} X {n} = {i*n}")


number = int(input("Enter any number : "))
printTable(number)
