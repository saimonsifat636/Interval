
# a = int(input("please enter 1st number: "))
# b = int(input("please enter 2nd number: "))
# try:
#     print(f"div of two num {a/b}")
# except TypeError as d:
#     print(d)
# except Exception as e:
#     print(e)
# else :
#     print("no exception is occured.")









# Finally -> we use it mainly when we are working with fucntion .
def student(age,height):
    try:
        ratios=age/height
    except Exception as e:
        print(e)
    finally:
        print("ALL is Well!")

student(12,'j')