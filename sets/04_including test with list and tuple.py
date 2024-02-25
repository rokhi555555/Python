a=set()


#list include test
#a.add([4,6,7])
# will not include list and through error TypeError: unhashable type: 'list'
#print(a)


#tuple included test 
a.add((1,7,9))
a.add(4)
print(a)


#hasable means that they immutable

#including dic test
# a.add({"name":6}) # also cannot add dic to sets bc it is not hashable
print(a)