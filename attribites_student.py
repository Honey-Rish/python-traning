class Student:
    # Class attributes / static variables
    courses = {'JAVA': 5000, 'PYTHON': 6000, 'REACT': 4000}

    @staticmethod
    def get_fee(course):
        return Student.courses.get(course.upper(), None)

    def __init__(self, admno, name, course):
        if course.upper() not in Student.courses:
            raise ValueError("Invalid Course!!")

        # Object attributes
        self.admno = admno
        self.name = name
        self.course = course
        self.fee_paid = 0

    def payment(self, amount):
        self.fee_paid += amount

    def get_total_fee(self):
        return Student.courses[self.course.upper()]

    def get_due(self):
        return self.get_total_fee() - self.fee_paid


print(Student.get_fee('Python'))

s1 = Student(1, "Ram", "Java")
s2 = Student(3, "John", "Python")

s1.payment(2000)
s2.payment(3000)

print(s1.get_due())
print(s2.get_due())