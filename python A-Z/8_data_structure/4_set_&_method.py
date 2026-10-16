sets={22,33,52,21,75,43,21}   # ->This is denoted by {} ,  every element must be unique.
print(sets)
# print(sets[1])   -> So, this can't be possible in sets.
#Method for set.
sets.add(23)
sets.add(3)
sets.remove(33)
sets.discard(22)  # ->this will remove a element from the set , If it is in there . It won't give error.
sets.discard(2)
print(sets)