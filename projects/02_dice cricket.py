import random


print("Dice cricket")
print("Computer's turn : score from 1 to 6")
comp = random.randint(1,6)
you = int(input("Your turn: enter in from 1 to 6"))


def game_res(comp,you):
   if comp==you:
     return False
   else:
      return True

res= game_res(comp,you)
if res :
   print("you win")
else:
   print("You lose")


# while you>0 and you<7:
#     you=you+you