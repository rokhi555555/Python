
#logical  and operator


age = int(input("Enter your age "))
if(age>=18 and age<=60): 
            # and returns false if one  of inputs is false
    print("you can vote")
else:
    print("You cannot vote ")

pasport = False
id_card =True
if(pasport or id_card):  # or truns true if one of inputs is true
    print("You can enter to Hall")
else:
    print("Access denied \n try again")