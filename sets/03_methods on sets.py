#creating empty set
# sts are collection of distinict(non-repeated) objects
eset =set()
print(type(eset))



#adding elemnts to set
# Add an element to a set.
# This has no effect if the element is already present.
eset.add(4)
eset.add(6)  # will add them in set in ordered manner
eset.add(3)
print(eset)
# remember that sets not have repeatation
# adding a vale repearedly doesnot make any change
eset.add(6)
eset.add(6)
eset.add(6) #not will include bc repeation is not allowed
print(eset)