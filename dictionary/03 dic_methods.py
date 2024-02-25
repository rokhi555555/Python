# dictionary methods


#keys

mydic ={
    "names":"ali",
    "shizuka":'girl',
    "marks":[2,4,5,7,8],
    4:'you'
}
print(mydic.keys())   # print keys
print(type(mydic.keys())) # printing type of keys  -->dic_keys
print(list(mydic.keys())) #printing keys in list


#printing values 
print(mydic.values())
print(list(mydic.values())) # vales printed in list
print(type(mydic.values())) #type of vale --> dic_values


# items-->  to pprint all keys,values of all elemnts of dictionary
print("\n")
print(mydic.items())



#update with adding key pairs
updic ={
    "book":78,
    "handbag":"moien",
}
# just like it pushes key -value pairs to dicn
mydic.update(updic)
print(mydic)


#dic_name.get("key") -->gets value at thatt kry
print(mydic.get("marks"))