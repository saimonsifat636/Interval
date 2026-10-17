class point:
    def  __init__(self,x,y):
        self.x=x
        self.y=y
    def sum (self,p):
        return (self.x+p.x,self.y+p.y)
    def __add__(self,p):
        return (self.x+p.x,self.y+p.y)

p1=point(3,4)
p2=point(5,4)
#overloading manully
p=p1.sum(p2)
#better waY TO DO THIS OVERLOADING.
p_=p1+p2

print(p)
print(p_)
