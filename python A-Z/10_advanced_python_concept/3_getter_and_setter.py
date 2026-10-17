#basic method to change a person first name

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def get_info(self):
        print(f"my name is {self.name}and i am about {self.age}.")
    def first_name(self):
        l=list(self.name.split())
        return l[0]
    def change_first_name(self,new_name):
        l=list(self.name.split())
        l[0]=new_name
        return " ".join(l)


p1=person('saimon sifat sanim',23)
p1.get_info()
print(p1.first_name())
print(p1.change_first_name("minas"))








# Property method:

#basic method to change a person first name

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def get_info(self):
        print(f"my name is {self.name}and i am about {self.age}.")

    @property   # now it will act as a property nat as an attribute.
    def first_name(self):
        l=list(self.name.split())
        return l[0]
    
    @first_name.setter    # we can set this using the property
    def first_name(self,new_name):
        l=(self.name.split())
        l[0]=new_name
        self.name=" ".join(l)


p1=person('saimon sifat sanim',23)
p1.get_info()
print(p1.first_name)
p1.first_name="karim MBSTU"
print(p1.first_name)
p1.get_info()

