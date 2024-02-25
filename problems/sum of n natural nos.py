num =int(input("Enter any number"))
numb =num+1
sum =0
for i in range(1,numb):
  sum = i+ sum
# print(i)
#   print(sum)
print("sum of natural nos less then "+ str(num) +" is :" +str(sum))