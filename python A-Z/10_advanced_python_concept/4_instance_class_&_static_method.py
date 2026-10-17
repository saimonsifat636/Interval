class student:
    university='MBSTU'

    # this is an instance method that's why we always need to give "self"  as an perameter.
    def __init__(self,name,age):
        self.name=name
        self.age=age


    @classmethod # -> this is a class method . We use it to make change on class attribute . We need to give a decorator called "@classmethod " to apply this and also need to give a perameter called "cls" .
    def change_varsity(cls,new_uni):
        cls.university=new_uni



    @staticmethod   # -> this is a static method . We use it to make change only on that function that is not dependent on instance or class  attribute . We need to give a decorator called "@staticmethod " to apply this and also no need to give perameter .
    def check_eligibility(age):
        return age>=18
    def info(self):
        print(f"my name is {self.name}, I am {self.age} years old.")





s1=student("karim ",18)
s1.info()
print(student.university)
s1.change_varsity("khulna")
print(student.university)
print(s1.check_eligibility(12))