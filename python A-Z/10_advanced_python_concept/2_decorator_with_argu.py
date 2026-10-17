def repeater(n):
    def decorator(func):
        def wraper(a):
            for i in range(0,n):
                func(a)
        return wraper
    return decorator

'''
here 
def repeater(n):   -> this will reapeat the process n times.
    def decorator(func):  -> this will give the function
        def wraper(a):      -> this will execute that function
            for i in range(0,n):
                func(a)
        return wraper
    return decorator
'''
@repeater(5)
def say_hello(a):
    print(f"hello {a}")

say_hello("karim")