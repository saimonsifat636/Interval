# while True:
#     try:
#         a = int(input("please enter 1st number: "))
#         b = int(input("please enter 2nd number: "))
#         print(f"sum of two number { a + b }")
#     except Exception as e:
#         print(e)


a = int(input("please enter 1st number: "))
b = int(input("please enter 2nd number: "))

if b==0:
    raise ValueError("please don't give zero as a value.")  # -> we use this to throw an error to prevent unnecessary execution of line.
print(f"DIv of two number { a / b }")