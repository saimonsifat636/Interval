marks=[32,99,93,85,77]
mixed=['sanim',99,3.85,True]    # this is called List and this is mutable -> we can change it unlike string that can't be changed.

print(marks[2:5])
print(mixed[:4])


#list   module :::
marks.extend(mixed)
print(marks)
marks.append(10000)
print(marks)

#list comprehention::
table=[]

for i in range(1,11):
    table.append(i*5)

print(table)

# using list comprehention way
table1=[i*5 for i in range(1,11)]
print(table1)