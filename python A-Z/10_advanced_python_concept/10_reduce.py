from functools import reduce


numbers=[1,2,3434,5,67,2,43,12,7]
print(numbers)
app=reduce(lambda x,y:x+y,numbers )
print(app)