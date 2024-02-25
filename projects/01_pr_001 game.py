import random

print("Computer's turn: water(1),snake(2),gun(3)")
no = random.randint(1,3)
# print(no)
if no==1:
    comp="w"
elif no==2:
    comp ="s"
elif no==3:
    comp ="g"

you=input("Player trun: water(w),snake(s),gun(g)")
def gamresult(comp,you):
 if comp ==you:
    return None
 
 elif comp=="w":
    if you =="s":
       return True
    elif you=="g":
       return False
    
 elif comp=="s":
    if you =="g":
       return True
    elif you=="w":
       return False
    
 elif comp=="g":
    if you =="w":
       return True
    elif you=="s":
       return False
print(f"computer turn {comp}")
print(f"your turn {you}")
a= gamresult(comp,you)
if a is None:
   print("Game Tied......")
elif a:
   print("......You Won the game ")
else:
   print("You Lose the game....")