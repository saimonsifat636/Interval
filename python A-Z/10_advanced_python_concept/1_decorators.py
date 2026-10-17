def decorator(func):
    def wrapper():
        print("what a lovely day .")
        func()
        print("to my friend.")
    return wrapper


@decorator
def say_hello():
    print("hello ! ")


  
say_hello()


# f=decorator(say_hello)
# f()