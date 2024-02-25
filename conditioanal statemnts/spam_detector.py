text = input("Enter text here")
if("get rewards" in text):
    spam =True
elif("click link" in text):
    spam =True
elif("earn money" in text):
    spam =True
elif("subscribe" in text):
    spam =True
elif("claim your bonous" in text):
    spam =True
else:
  spam= False

if(spam is True):
    print("Beware, This is a spam . ")
else:
    print("Relax guys this is not a spam")