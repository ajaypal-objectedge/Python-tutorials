# print a pattern of diamond with input of no. of rows (odd only)

rows = int(input("Enter the odd number of rows"))
spaces = int(rows/2) 
stars = int(1) 

for row in range(0,rows) :
    if row < int(rows/2):
        for space in range(0,spaces):
            print(" ",end=" ")
        for star in range(0,stars):
            print("*",end=" ")
        for space in range(0,spaces):
            print(" ",end=" ")
        spaces = spaces - 1
        stars = stars + 2   
        print("\r")  
    else :
        for space in range(0,spaces):
            print(" ",end=" ")
        for star in range(0,stars):
            print("*",end=" ")
        for space in range(0,spaces):
            print(" ",end=" ")
        spaces = spaces + 1
        stars = stars - 2
        print("\r")    
