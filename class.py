
class Student :
    def __init__(self,name,roll_no,hobby) :
        self.name = name
        self.roll_no = roll_no 
        self.hobby = hobby

    def __str__(self):
        return f"{self.name}{self.roll_no}{self.hobby}"

    def getInfo(self):
        print(self.name + "  is roll no. " + str(self.roll_no) + " and likes " + self.hobby)  

# class boy inherits the property of class Student
class boy(Student) :  
  #  pass  : only pass will directly enable inheritance
  def __init__(self, name, roll_no, hobby,place):
     # Student.__init__(self, name, roll_no, hobby)
     super().__init__(name,roll_no,hobby)
     self.place = place    # adding additional property           
       
student1 = boy("Ajay",21,"Football","Agra")
student2 = boy("Dhanesh",13,"Swimming","Mumbai")

temp = student2
student2 = student1
student1 = temp

#print(student1.name + " " + str(student1.roll_no) + " " + student1.hobby)
#print(student2.name + " " + str(student2.roll_no) + " " + student2.hobby)

student1.getInfo()
student2.getInfo()

print(student1.place)
print(student2.place)