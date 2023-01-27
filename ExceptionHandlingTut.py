
try:
    print("hello")
except NameError:
    print("x is not defined")
except :
    print("Something went wrong")    
else :
    print("Nothing went wrong")
finally :
    print("try - except got done")    


# we can also raise any Exception as per condition required

x = 5 

if x % 2 != 0 :
    raise Exception("Invalid value for x")
