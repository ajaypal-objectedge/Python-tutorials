# Print all prime numbers between the range x (User input) and y (user input) 

X = input("Enter the lower value")
Y = input("Enter the highest value")

x = int(X)
y = int(Y)

import math

for num in range(x,y+1):
    isPrime = True 
    for div in range(2,int(math.sqrt(num)) + 1) :
        if num % div == 0 :
            isPrime = False 
            break 

    if isPrime == True :
        print(num)
        


