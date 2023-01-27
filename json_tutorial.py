# JSON stands for Java Script Object Notation
# JSON is a syntax for storing and exchanging data
import json

def printAllPairs(x):
    allItems = x.items()
    for i in allItems:
        print(i)

person1 = {                 # dictionary
    "Name" : "Ajay",
    "DOB" : "05 Nov 1998",
    "Place" : "Agra"
}

# JSON string 
person2 = '{ "Name" : "Pushpesh" , "DOB" : "16 july 1994" , "Place" : "Delhi"}'

#print(type(person1))
#print(type(person2))

# to convert json string to python dictionary we use below fuction:
person3 = json.loads(person2) 

#print(type(person3))

#printAllPairs(person1)
#printAllPairs(person3)

# to convert python dictionary to JSON string we use dumps function mentioned below
person1 = json.dumps(person1)

#print(type(person1))
"""
# python objects can be converted into JSON string using the dumps function:

print(json.dumps({"name": "John", "age": 30})) #dictionary 
print(json.dumps(["apple", "bananas"]))        #list
print(json.dumps(("apple", "bananas")))        #Tuple
print(json.dumps("hello"))                     #String
print(json.dumps(42))                          #int                             
print(json.dumps(31.76))                       #float                     
print(json.dumps(True))                        #True             
print(json.dumps(False))                        #False
print(json.dumps(None))                         #None

"""
# Converting a python object (dictionary containing values of different data types or collections) into a single JSON string



x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# the printed string will not be easier to read without indentation and line breaks
print(json.dumps(x))

# we have indent parameter to json.dumps() to make it readable 
print(json.dumps(x, indent=4))