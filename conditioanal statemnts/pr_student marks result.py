sub1= int(input("enter marks in sub1 : "))
sub2= int(input("enter marks in sub2 : "))
sub3= int(input("enter marks in sub3 : "))
sub4= int(input("enter marks in sub4 : "))

sum=sub1+ sub2+sub3+ sub4

if(sub1<33 or sub2<33 or sub3<33 or sub4<33): #by this or by below 
                    # if(not(sub1>33 and sub2>33 and sub3>33 and sub4>33)):
    print("You failed due to less then 33% marks in one subject")
elif(sum/4)<40:
    print("you failed due to total precentage less then 40%")
else:
    print("You Passed")