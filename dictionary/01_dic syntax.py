
#creating a  dictionary 
'''
dic_name={
  "key":"value"
    value may be int,string,float,bool,list---> , is essential at every def but not for last defn
}

'''
mydic ={
    "fg":"federal govt ",  #string
    "rollno":9,    #int
    "marks":[1,11,21,31],   #list
    "noob":True
}
print(mydic['fg'])
print(mydic['rollno'])
print(mydic['marks'])
print(mydic['noob'])

# dic is mutable/changeable,no duplicate keys,dic is unordered
mydic['rollno']=65
print(mydic['rollno'])
