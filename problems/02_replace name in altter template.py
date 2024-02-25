letter = '''          <Date>
Dear<!name!>
   hope you are fine....
      Your's sincerely
         <!name!>
'''
name = input("Enter your name here")
date =  input("enter date")+"/2023"
letter=letter.replace("<!name!>",name)
letter=letter.replace("Date",date)
print(letter)
