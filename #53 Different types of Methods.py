#53 Different types of Methods
class Student:

  school = 'Baxton University'

  def __init__(self,mark1,mark2,mark3): #(marks are the marks which the student ot)
    self.mark1 = mark1
    self.mark2 = mark2
    self.mark3 = mark3

  #we now want to know the avarage mark of the student
  #this is an instance method since we are using instance (variables)
  def avg(self):
    return(self.mark1 + self.mark2 + self.mark3)/3

  @classmethod #(this is a decorator)
  def schoolattended (cls):
    return cls.school

  @staticmethod
  def studentinformation():
    print( "this is student class ... in dev module")

#objects
s1 = Student(10,12,15) #the arguments are the student marks
s2 = Student(20,10,15)

#instance method
print(s1.avg())
print(s2.avg(),'\n')

#the class method
print(Student.schoolattended()) #preferable we use this line of code
# print(s1.schoolattended(),'\n') #or we can use this from our method

#static module
Student.studentinformation() #prefarable we use this line of codde
# print(s1.studentinformation()) #by using object


