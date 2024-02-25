no1 = int(input("Enter no1 : "))
no2 = int(input("Enter no2 : "))
no3 = int(input("Enter no3 : "))
no4 = int(input("Enter no4 : "))
'''
suppose this as nockout stage of cricket world cup
among 4 qualifing teams two semifanals are played
and both winners of semis meetup in final .
and the winner of finale is champ

'''

if(no1>no2):  # semifinal 1   
    f1=no1
else:
    f1=no2

if(no3>no4):   # semi final 2
    f2=no3
else:
    f2=no4

if(f1>f2):    # final
    print(f1," is greatest")
else:
    print(f2, " is greatest")
