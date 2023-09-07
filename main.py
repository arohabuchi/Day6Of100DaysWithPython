################################### Enum #####################################
from enum import Enum

class color(Enum):
    red = 1
    green = 2
    blue = 3
    yellow = 4

print(color.red)
print(color(1))
print(color['red'])
######################### Enum iteration ############################
from enum import Enum
class color(Enum):
    red = 1
    green = 2
    blue = 3
    yellow = 4

for c in color:
    print(c)

print([c for c in color])

############################################ TOPIC 2  #######################################################
################################################  SET IN PYTHON {} #####################################################
#remember we did intro to set in our day 4 class
#Operations on set
x = {1,2,3,4}
v = {3,4,5,6,7,}
# a. Intersection
a = {1,2,3,4}.intersection({3,4,7,8,9})
b ={1,2,3,4} & {3,4,7,8,9}
print(a)
print(b)

#union
x = {1,2,3,4}
v = {3,4,5,6,7,}
u=x.union(v)
u2 = x|v
print(u)
print(u2)

#difference
x = {1,2,3,4}
v = {3,4,5,6,7,}
d=x.difference(v)
d1=x-v
print(d)
print(d1)


#symmetric difference
x = {1,2,3,4}
v = {3,4,5,6,7,}
d=x.symmetric_difference(v)
d1=x^v
print(d)
print(d1)

#superset check
x = {1,2,3,4}
v = {3,4,5,6,7,}
d=x.issuperset(v)
d1=x>=v
print(d)
print(d1)

#subet check
x = {1,2,3,4}
v = {1,2,3,4,5,6,7,}
d=x.issubset(v)
d1=x<=v
print(d)
print(d1)

#dijoint check
x = {1,2,3,4}
v = {3,4,5,6,7,}
vi={7,9,8,10}
d=x.isdisjoint(v)
d1=x.isdisjoint(vi)
print(d)
print(d1)

################################################ with ssingle element #################################################################

#existence check

x = 3 in {1,2,3,4}
y = 8 in {1,2,3}
v = 7 not in {3,4,5,6,7,}
print(x)
print(v)
print(y)

#add or remove
x = {1,2,3,4}
v = {3,4,5,6,7,}

x.add(9)
print(x)

x.discard(2)
print(x)
x.discard(0)
print(x)

x.remove(3)
print(x)

######################################### Get unique element of a list #####################################
#you have a list with different items which many of the items appears multiple times. now you want to get unique element from the list

items=['apple','pear','apple','orange','mango','pear','orange','mango','tomato','tomato','apple','pear','pear','pear','mango',]
uniqueItems=set(items)  #convert it to set
print(uniqueItems)
backToLit=list(uniqueItems) #convert back to list
print(backToLit)

#using single line
s=list(set(items))
print(s)
