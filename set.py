# unordered , iterable , mutable but set items are unchangeable , not allow duplicate values
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
anotherset = {"icecream" , "choclate"}
anotherset.remove("icecream")
thisset.update(anotherset)
print(thisset)





