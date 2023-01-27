# Use of copy statement help us to only change the required collection keeping the other one as it is

list1 = ["apple","banana","mango"]
list2 = []
list2.extend(["football","cricket"])
#list3 = list1 
list3 = list1.copy()
list3[0] = "I am changed"
print(list1) 
print (list3)