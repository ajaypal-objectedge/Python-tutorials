"""
myTuple = ("Apple" , "Mango" , "Guava")
myit = iter(myTuple)

print(next(myit))
print(next(myit))
print(next(myit))

myStr = "Ajay"
myitStr = iter(myStr)

print(next(myitStr))
print(next(myitStr))
print(next(myitStr))
print(next(myitStr))

"""

# myit is an iterator over myTuple
# myitStr is an iterator over myStr
# For loop basically creates an iterator object and executes next for each loop
# For each class/object to be iterable we have to write and __iter__ and __next__ methods

class myNumbers :
    def __iter__(self):
        self.a = 1 
        return self 

    def __next__ (self):
        if self.a < 20 :
            x = self.a
            self.a += 1 
            return x 
        else:
            raise ValueError  

myClass = myNumbers()
myiter = iter(myClass)

for x in myiter:
    print(x)