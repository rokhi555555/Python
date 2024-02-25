# length of set
a ={2,6,7,9}
print(len(a)) #prints no of elements in set 
# line(5)remember if set contains tuple then it will be counted as a single element
a.add((4,6,8)) # adding tuple
print(a)

# removing elements of set
a.remove(6) # removes 6
print(a)
# it will through error if removing element is not in set
# a.remove(3) #' 3' is not in set a
print(a)

#set.pop()-->removes any elemnt
dset ={5,7,(1,2),8,9,0}
dset.pop()  # pop takes no argument
print(dset)
