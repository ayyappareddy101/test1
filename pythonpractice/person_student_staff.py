


class Person:
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def name(self):
        return self.first_name+ " " +self.last_name


class Student(Person):
    count = 0
    def __init__(self, first_name, last_name, rollno, mark1, mark2):
        super().__init__(first_name, last_name)
        self.rollno = rollno
        self.mark1 = mark1
        self.mark2 = mark2
        Student.count += 1
    def GetStudent(self):

        return f'Student name: {self.first_name + ' '+self.last_name},Roll No:{self.rollno},Total Marks:{self.mark1 + self.mark2}'

class Staff(Person):
    count = 0
    def __init__(self, first_name, last_name,staffnum):
        super().__init__(first_name,last_name)
        self.staffnum = staffnum
        Staff.count += 1
    def GetStaff(self):
        return f'StaffName: {self.first_name+' '+self.last_name},StaffNumber: {self.staffnum}'

#
# p = Person()
# print(p.name())

# s = Student('sai','ram', 375, 78, 85)
# print(s.GetStudent())
#
# staff = Staff('srinivas','master', 420)
# print(staff.GetStaff())

if __name__ == '__main__':
    s1 = Student('sai', 'ram', 375, 78, 85)
    s2= Student('ganesh', 'reddy', 999, 98, 55)
    s3 = Student('Deepu', 'nani', 645, 99, 70)
    lst = [s1,s2,s3]
    for i in lst:
        print(i.GetStudent())

    print(Student.count)