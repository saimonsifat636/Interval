try:
    a=int(input("enter the 1st num : "))
    b=int(input("enter the 2nd num : "))
    o = input("operator: ")
    match o:
        case "+":
            print(f"sum : {a+b}")
        case "-":
                    print(f"sub : {a-b}")
        case "/":
                    print(f"div : {a/b}")
        case "*":
                    print(f"Mul : {a*b}")
        case _ :
                    print("choose proper operator.")
except ZeroDivisionError:
        print("please put value greater than 0!")        
except Exception as e:
        print("please put a valid number ")