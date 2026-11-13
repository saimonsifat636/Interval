import numpy as np



#integers:
rng=np.random.default_rng()   #here when seed=1 it will return the same output.
print(rng.integers(low=1,high=10,size=(1,2)))


#float:
np.random.seed(seed=0)
print("\n\n\n")
print(np.random.uniform(low=1,high=10,size=(4,4)))
print("\n\n\n")



#shuffle card:
array=np.array([1,2,3,4,5,6,7,8])
rng.shuffle(array)
print(array)
print("\n\n\n")



#choice:
fruits=np.array(["aaaa","dasfda","adfasd","fadadasdfasdfa"])
fruits=rng.choice(fruits,size=1)
print(fruits)