class Student:
    def __init__(self, name, age, contact, marks, address):
        self.name = name
        self.age = age
        self.contact = contact
        self.marks = marks
        self.address = address

    def __str__(self):
        return "Name is :{}\n" \
               "Age is :{}\n" \
               "contact is :{}\n" \
               "Address is :{}\n" \
               "Marks is :{}\n".format(self.name, self.age, self.contact, self.address, self.marks)


def menu():
    print('---MAIN MENU---')
    print('1. To add a student')
    print('2.To show all students')
    print('3. Exit')


if __name__ == '__main__':
    studentlist = []
    menu()
    userInp = int(input('please enter the choice of above menu'))
    runagain = True
    while True:
        if userInp == 1:
            while runagain:
                name = input("ENTER THE NAME")
                age = int(input("ENTER THE AGE"))
                contact = input("ENTER THE CONTACT")
                marks = input("ENTER THE MARKS")
                address = input("ENTER THE ADDRESS")
                values = Student(name=name, age=age, contact=contact, marks=marks, address=address)
                studentlist.append(values)
                cursor = input('press y to add more OR any key to exit')
                if cursor[0] == 'y':
                    runagain = True
                else:
                    runagain = False
                menu()
            userInp = int(input("ENTER UR CHOICE"))
        elif userInp > 3 or userInp <1:
            print('Invalid Input detected')
            menu()
        userInp =int(input('Please enter the choice from above'))