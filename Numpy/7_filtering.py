import numpy as np

ages=np.array([[11,2,22,3,33,55,74,90],
               [88,22,41,18,14,25,99,100]])
print(ages.shape)


# filtering:

teenage=ages[ages<=18]
adults=ages[ages>18]
elder=ages[ages>=65]
man=ages[(ages>18) & (ages<65)]
print(f"teenages   :  {teenage}")
print(f"adults   :  {adults}")
print(f"elder   :  {elder}")
print(f"man   :  {man}")

# If we want to filter them without changing their shape then we need to use "where()" function -> where(condition,list,default)

pas = np.where(ages>=33,ages,np.nan)
print(pas)