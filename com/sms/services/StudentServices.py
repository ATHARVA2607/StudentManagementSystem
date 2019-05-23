from com.sms.objects.Student import Student
from com.sms.utils.ReadUtils import  ReadUtils

class StudentServices:
    reader=ReadUtils()
    students=[]
    def addStudent(self):
        s=Student(
            name=  self.reader.ReadUserInputStr('Please Enter The Name ',"Error Try Again"),
            age= self.reader.ReadUserInputInt('Please Enter the age',"error"),
            contact=self.reader.ReadUserInputStr('Please Enter the Contact Number','Error'),
            marks=self.reader.ReadUserInputInt('Please Enter the Marks ','Error'),
            address= self.reader.ReadUserInputStr('Please Enter the Contact Number', 'Error'),
        )
        self.students.append(s)
        #send Mail

    def viewAllStudents(self):
        for d in self.students:
            print(d.__str__())

    def viewStudentById(self):
        pass