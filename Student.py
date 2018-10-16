class Student:
    def __init__(self, name, rno, markList):
        self.name = name
        self.rno = rno
        self.markList = markList

    def display(self):
        print('Name: {}'.format(self.name))
        print('Roll no.: {}'.format(self.rno))
        self.markList.display()
        

class MarkList:
    def __init__(self, maths, hindi, marathi, english, science):
        self.maths = maths
        self.hindi = hindi
        self.marathi = marathi
        self.english = english
        self.science = science
    
    def display(self):
        print('Marks: ')
        print('Maths: {}'.format(self.maths))
        print('Hindi: {}'.format(self.hindi))
        print('Marathi: {}'.format(self.marathi))
        print('English: {}'.format(self.english))
        print('Science: {}'.format(self.science))

    def totalMarks(self):
        return self.maths + self.marathi + self.hindi + self.english + self.science

    def percentageMarks(self):
        return (self.totalMarks()/500.0) * 100
        
class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students

    def display(self):
        print('Name: {}'.format(self.name))
        for stu in self.students:
            stu.display()
            print('')

    def getNumberOfStudents(self):
        return len(self.students)
    
    def getAveragePercentage(self):
        sum = 0.0
        for stu in self.students:
            sum += stu.markList.percentageMarks()
        return sum/self.getNumberOfStudents()

    def getIntelligentStudent(self):
        maxMarks = max(stu.markList.totalMarks() for stu in self.students)
        for stu in self.students:
            if stu.markList.totalMarks() == maxMarks:
                return stu
        return None

    def getDullStudent(self):
        minMarks = min(stu.markList.totalMarks() for stu in self.students)
        for stu in self.students:
            if stu.markList.totalMarks() == minMarks:
                return stu
        return None

m1 = MarkList(60, 80, 98, 72, 89)
s1 = Student('Vaibhav', 1, m1)

m2 = MarkList(79, 87, 93, 85, 99)
s2 = Student('Varun', 2, m2)

m3 = MarkList(70, 75, 92, 79, 88)
s3 = Student('Ajinkya', 3, m3)

m4 = MarkList(78, 82, 85, 94, 78)
s4 = Student('Vishwajeet', 4, m4)

m5 = MarkList(98, 80, 67, 40, 68)
s5 = Student('Aditya', 5, m5)

studentList = [s1, s2, s3, s4, s5]
mySchool = School('My School', studentList)

mySchool.display()
print("Number of students: {}".format(mySchool.getNumberOfStudents()))
print('Average: {}'.format(mySchool.getAveragePercentage()))

stu = mySchool.getIntelligentStudent()
stu.display()

stu = mySchool.getDullStudent()
stu.display()