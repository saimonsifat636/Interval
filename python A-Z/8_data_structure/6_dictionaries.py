marks={"saimon":22,"karim":44,"sakin":55,"abdullah":66,"lily":90}
# -> These are the dictionaries and they are denoted by {kyes , values }


print(marks)

#methods:
print(marks.keys())
print(marks.values())
marks.pop("lily")  #-> this will remove lily from the dectionary.
print(marks)
marks.clear() # this will clear all the element from the dictionary
print(marks)



# comprehention of dectionaries:
table_of_5={i:i*5 for i in range(1,11)}
print(table_of_5)