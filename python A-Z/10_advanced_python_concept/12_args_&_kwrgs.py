#*args -> we use args when we don't know how many arguments are gonna be there , we can take as many as we want using *args . It will make them or store them as  Tuples.

# **kwrgs -> we use it when we need to pass info , It convets/store them as dictonaries
 
#   *args 
from functools import reduce

def sum(*args):
    print((reduce(lambda x,y:x+y,args)))

sum(1,2,6,4,8,7,7)  # Here we are giving a lot of arguments without initializing perameter.




#   **kwrgs
from functools import reduce

def marks(**kwrgs):
    print("\n\n",kwrgs)

marks(saimon=11, karim=22, rafiq=55, shamim=88, kabir=99, saimon_2=77, sifat=88)

 # Here we are giving a lot of info without initializing perameter.


 #  combine both *args and **kwrgs 
 # TO do this we need to maintain a format where always first perameter will be *args and 2nd will be **kwrgs

 
def position(*args,**kwrgs):
    print("\n\n",args,"\n\n",kwrgs)

position(1,2,3,4,5,6,7,saimon=11, karim=22, rafiq=55, shamim=88, kabir=99, saimon_2=77, sifat=88)


 