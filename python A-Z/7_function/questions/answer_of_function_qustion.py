#1 
#1.1
def greet():
    print("hello world")

greet()

#1.2
import math
print(math.sqrt(49))

#2
#2.1
sum=lambda x,y:x+y

print(sum(3,7))

#2.2
numbers=[1,2,3,4,5,6]
result=map(lambda x: x**2,numbers)
print(list(result))


#3
#3.1
def factorial(n):
    if(n<=1):
        return 1;
    return factorial(n-1)*n

n=int(input("Give a number that you wanna find the factorial of that: "))
print(f"factorial of {n} is : {factorial(6)}")


#3.2
def sumofdigit(n):
    if n==0:
        return n
    return n+sumofdigit(n-1)

print(f"sum of digit are: {sumofdigit(n)}")