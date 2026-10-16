#1
name="saimonsifatsanim"
print(name[0])
print(len(name))
print(name[15])


#2
print(name[0:7])
print(name[-6:])
print(name[::-1])

#3
text=" i love python programming "

print(text.strip())
print(text.lstrip().title())
print(text.count("o"))

newtext="1234abx"

print(newtext.isalnum())


#4
name="jhon"
age=23

print(f"my name is {name} and I am {age} years old.")


#5
sentence="coding in python is fun"
sentence = sentence.replace("fun", "awesome")
print(sentence)
print(sentence.find("python"))
print(sentence.upper())

#bonus question 
newsentence="coding in python is fun"
vowels=['a','e','i','o','u']
sum =0
for char in newsentence:
    if(char in vowels):
        sum+=1

print(f"\nthere are {sum} vowels in this sentence.\n")



#palindrome check
info=input("please give what you wanna check: ")
if(info==info[::-1]):
    print("this is palindrome.")
else:
    print("not a palinedrome. ")