mydict={
    "Subh":"morning",
    "Sham":"Evening",
    "raat":"Night"
}
print(mydict.keys())
# print(type(mydict.values()))
a = input("Enter any urdu word\n")
# print("english meaning is : ",mydict[a])# if user enter other name it will show error
# so to preventing from error we will use this below line
print("english meaning is : ",mydict.get(a))
# if user enter other name it will not show error

