class  employee:
    agent="boe jhon"
    def __init__(self,name,salary,year_of_join,agent ):    # this _init_ create a constructor that is able to assign values form the object .
        self.name=name
        self.salary=salary
        self.year_of_join=year_of_join
        self.agent=agent

    def get_info(self):
        return (f"the name of this emp is {self.name} and his salary is {self.salary}  , he join in {self.year_of_join}. He come here throught this agent called {self.agent}.")
    def company(self):
        return "xyzC ..vo"



e1= employee("karim ", 24000,2018,"tvf")
print(e1.get_info(),"\n")
print(e1.company(),"\n")
print(employee.agent)    #IF we want to print the class attribute rather than the object or instance attributes we can use CLASS_NAME.attributes.




# for object introspection 
print(dir(e1))
        