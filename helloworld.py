"""
print("Hello world")
print("Ajay is learning python")

x = 1 
y = "Ajay"
z = 'Ajay'
a = str(3) 
b = int(3)
c = float(3)


print(x , y , z ) #+ " " + a + " " + b + " " + c )

print(type(a))
print(type(b))
print(type(c))
print(type(y))
print(type(z))

"""

"""
To print words from sentences

text = "Ajay is learning python" 
startIndex = 0 
endIndex = 1 
for eachText in text :
    if endIndex == len(text):
        print(text[startIndex:endIndex])
        break 
    ch = text[endIndex] 
    if ch == " " :
        print(text[startIndex:endIndex])
        startIndex = endIndex+1
        endIndex = startIndex
    else:
        endIndex = endIndex + 1 

"""
'''text = "Ajay is learning python" 
print(text.split("arn")) 
'''

condition = {}

if condition :
    print("Evaluated as true")
else:
    print("Evaluated as false")


        




