from com.sms.utils.ReadUtils import ReadUtils
from com.sms.services.StudentServices import StudentServices


def printMenu():
    print("Main Menu \n1. Add Student\n2. Show All Students")


s = StudentServices()

def getCase(val):
    switcher = {
        1: s.addStudent,
        2: s.viewAllStudents,
        3: s.viewStudentById
    }
    #print( switcher.items())
    return switcher.get(val)

if __name__ == '__main__':
    reader = ReadUtils()
    while True:
        printMenu()
        userInp = reader.ReadUserInputInt('Please Enter an Integer value from above menu', 'Please Try Again')
        ref = getCase(userInp)
        ref()
