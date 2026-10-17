#1

#1.1
fruits=["apple","banana","cherry"]
print(fruits)
fruits[1]="orange"
print(fruits)
print(len(fruits))

#1.2
num=[1,2,3,4,5,6,7,8,9,10]
print(num[:3]) # first three number using slicing.
print(num[-3:]) # last three number using slicing.



#2

#2.1
numbers=[5,3,9,1,7]
numbers.sort()
print(numbers)
numbers.append(10)
print(numbers)
numbers.remove(3)
print(numbers)

#2.2
names = ["Alice", "Bob", "Charlie"]
names.insert(1,"Devid")
print(names)


#3

coordinates=(10,20)
print(coordinates)
# coordinates[0]=50   # This will through an error because tuple are unmutable that's why it will generatre an error.
coordinates=list(coordinates)  # this will cast the tuple into a list.
print(coordinates)
coordinates[0]=50
print(tuple(coordinates)) # this will cast the list back to it's original form.




#4

#4.1
my_set={1,2,3,3,4}
print(my_set)
my_set.add(5)
my_set.discard(2)
print(my_set)


#4.2
a={1,2,3}
b={3,4,5}

c=a.union(b)
print(c)
d=a.intersection(b)
print(d)
e=a.difference(b)
print(e)




#5

#5.1
student={"name":"jhon","age":23,"grade":"A"}
print(student["name"])
student["grade"]="A+"
student["city"]="delhi"
print(student)


#5.2
print("\n\n")
for name,num in student.items():
    print(name," ",num)
print("\n\n")



#6 -> bonus questions.

#Basic way to take input in list using python 
# numbers=[]
# for i in range(0,11):
#     num=int(input("input: "))
#     numbers.append(num)
# print(numbers)


# this the shorter way to take input from the user and create a list. Remember the split function will split the string after each space ..
digit = list(map(int, input("Enter numbers: ").split()))

print(digit)
print(f"after using set ",set(digit))



#6.2
product={"ice-cream":123,"book":34,"toy":40}
print(product)
sum =0
for i  in product.values():
    if sum<=i:
        sum = i

print(sum)

#6.3
marks={"saimon":22,"karim":44,"sakin":55,"abdullah":66,"lily":90}
marged_directories={**product,**marks}
print(marged_directories)