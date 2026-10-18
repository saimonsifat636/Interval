# this is a technique to assign an attributes and it is denoted by ":=". It take a function output data so we don't need to call it again and again.

def slow_one():
    print("looding.......")
    print("looding.......")
    print("looding.......")
    print("looding.......")    
    print("looding.......")
    return 11

# Basic method:
if(slow_one()>10):
    print(slow_one(),"\ngreater than ten.")

print("\n\n\n")
# using warlus method :
if((a:=slow_one())>10):
    print(a,"\nGreater than ten.")  # -> in this method this is not calling again and again rather it is using once called value multiple time .


while((a:=input("please enter integer: "))):
    if a=='q':
        print("Exit done.")
        break
    print(a)