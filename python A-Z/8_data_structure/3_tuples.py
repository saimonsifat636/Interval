#Tuples are unmutable -> they can't be changed 
# list are denoted by  []      tuples are denoted by ()

name=('saimon','sifat','sanim','karim','tamim')
print(name)

# Tuple unpacking
tu=(11,22,44,66,77,22,11)
a,b,c,d,e,f,g=tu    #it will assing values into them so if we wanna print them using them we can do it.
print(a)
# we can also print value through indexing.
print(tu[1])




# Methods for tuples
marks=(11,22,22,222,22,44,66,77,22,11)
print(marks.index(22))     # -> this will return the index of that value.
print(marks.count(22))     # -> this will return the occurences of that value.