class animal:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
    def getinfo(self):
        print(f"animal={self.name} \nage={self.age}\nheight={self.height}")
    def speak(self):
        print("speaking now>>>>>>>>>")

class dog(animal):
    def speak(self):
        super().speak()   # this will return function that is in the parent class .
        print("barking....")



d=dog("Dog",2,5)
d.speak()
d.getinfo()