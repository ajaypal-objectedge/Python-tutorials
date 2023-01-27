# mySet = filter(lambda n:n % 8==0 ,)
# print(mySet)

# for i in range(25):
#     if i%8 == 0:
#         print(i)


# mySet = [num for num in range(100) if num % 8 == 0]
# print(mySet)

# mySetContaining6 = [num for num in range(100) if '6' in str(num)]
# print(mySetContaining6) 

string = "Practice Problems to Drill List Comprehension in Your Head."
# count = len([ch for ch in string if ch == " "])
# print(count)

# txt = "".join([ch for ch in string if ch not in ['a','e','i','o','u']])
# print(txt)

# find all the words in string having length < 5
listofwords = string.split(" ")
# list =  [word for word in listofwords if len(word) < 5]
# print(list)

# #Use a dictionary comprehension to count the length of each word in a sentence (use string above
# list = [len(word) for word in listofwords]  q8_answer = {num:max([divisor for divisor in range(1,10) if num % divisor == 0]) for num in nums}
# print(list)

list1 = range(1,100)
list2 = range(1,10)

list3 = {num:max([div for div in list2 if num % div == 0]) for num in list1}
#q8_answer = {num:max([divisor for divisor in range(1,10) if num % divisor == 0]) for num in list1}
print(list3)