def circle(r):
    area= 2*3.1416*r;
     # This is a local variable. It can't change the global variable.if you want to change the value from a local scope you need to declare it "Global" . SO , we can change it .
    global x   # This will help you to change the global variable.
    x=2  
    return area;



x=23  #this is a global variable. We can't change it. 
print(circle(5))
print(x)