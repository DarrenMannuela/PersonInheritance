class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def to_string(self):
        return f"{self.name}({self.address})"


class Teacher(Person):
    def __init__(self, name: str, address: str, num_courses=0):
        courses = {}
        super().__init__(name, address)
        self.num_courses = num_courses
        self.courses = courses
        self.courses.setdefault(self.name, [])

    def add_courses(self, course: str):
        if course not in self.courses[self.name]:
            self.courses[self.name].append(course)
            self.num_courses += 1
        else:
            return False

    def del_courses(self, course: str):
        if course in self.courses[self.name]:
            self.courses[self.name].pop(course)
            self.num_courses -= 1
        else:
            return False

    def to_string(self):
        return f"Teacher:{self.name}({self.address})"

    def print_courses(self):
        return f"Here are your courses{self.courses}"


class Student(Person):
    def __init__(self, name: str, address: str, num_courses=0):
        grades = {}
        courses = {}
        average = {}
        super().__init__(name, address)
        self.num_course = num_courses
        self.grades = grades
        self.courses = courses
        self.average = average
        self.courses.setdefault(name, [])

    def add_course_grade(self, course: str, grade: int):
        if course not in self.grades:
            self.grades.setdefault(course, [])
            self.grades[course].append(grade)
        else:
            self.grades[course].append(grade)

        if course not in self.courses[self.name]:
            self.courses[self.name].append(course)
        else:
            pass

    def get_average(self, course: str):
        total = 0
        for grades in self.grades[course]:
            total += grades
        average = total/len(self.grades[course])
        self.average.setdefault(course, average)
        return self.average

    def print_grades(self):
        return f"{self.name}\nHere are your grades for your courses: {self.courses[self.name]}" \
               f"\nAverage grades: {self.average}"

    def to_string(self):
        return f"Student:{self.name}({self.address})"


def main():
    print("Welcome to Get Some Help University")
    print("1.Student\n2.Teacher")
    choice = int(input("Are you a Student or a Teacher(1-2):"))
    if choice == 1:
        print("Welcome Student, what is your name")
        firstname = input("Firstname:").title()
        lastname = input("Lastname:").title()
        address = input("Address:").title()
        name = ('{} {}'.format(firstname, lastname))
        student = Student(name, address)
        while True:
            print("\nWelcome, how may we help {} ?".format(name))
            print("\n1.Add Course Grade\n2.Get Average Grade\n3.Get Grades\n4.Personal Info\n5.Back")
            do_what = int(input("\nWhat would you like to do(1-5):"))
            if do_what == 1:
                course = input("Course:").title()
                grade = int(input("Grade:"))
                student.add_course_grade(course, grade)
            if do_what == 2:
                course = input("Course:").title()
                student.get_average(course)
                print(student.average)
            if do_what == 3:
                print(student.print_grades())
            if do_what == 4:
                print(student.to_string())
            if do_what == 5:
                return False
            else:
                print("Invalid action")

    elif choice == 2:
        print("Welcome Teacher, what is your name")
        firstname = input("Firstname:").title()
        lastname = input("Lastname:").title()
        address = input("Address:").title()
        name = ('{} {}'.format(firstname, lastname))
        teacher = Teacher(name, address)
        while True:
            print("\nWelcome, how may we help {} ?".format(name))
            print("\n1.Add Course\n2.Delete course\n3.Personal Info\n4.Your courses\n5.Back")
            do_what = int(input("\nWhat would you like to do(1-5):"))
            if do_what == 1:
                course = input("Course:").title()
                teacher.add_courses(course)

            if do_what == 2:
                course = input("Course:").title()
                teacher.del_courses(course)

            if do_what == 3:
                print(teacher.to_string())

            if do_what == 4:
                print(teacher.print_courses())

            if do_what == 5:
                return False

            else:
                print("Invalid input")
    else:
        print("Invalid input")


if __name__ == "__main__":
    while True:
        main()
