class student:
    college='GCPSC'
    def __init__(self,name,age):  # this __init__ , __len__ , __repr__  are known as dunder /magic method.
        self.name=name
        self.age=age
    def __str__(self):
        return f"my name is {self.name} and I am about {self.age}."
    def __repr__(self):
        return f"name : {self.name} \nage : {self.age}"
    def __len__(self):
        return len(self.name)

s=student("saimon sifat",23)
print(str(s))
print(repr(s))
print(len(s))