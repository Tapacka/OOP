class Student:
    stud_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.stud_list.append(self)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecture, course, grade):
        if isinstance(lecture, Lecture) and course in self.courses_in_progress and course in lecture.courses_attached:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'

    def mark_list(self, marks_):
        lis = []
        for i in marks_.values():
            for a in i:
                lis.append(a)
        return lis

    def __str__(self):

        person = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка: {sum(self.mark_list(self.grades)) / len(self.mark_list(self.grades))} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)} \n'
        return person

    def __lt__(self, other):
        if isinstance(other, Student):
            avg_mark1 = sum(self.mark_list(self.grades)) / len(self.mark_list(self.grades))
            avg_mark2 = sum(other.mark_list(other.grades)) / len(other.mark_list(other.grades))

        return avg_mark1 < avg_mark2


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecture(Mentor):
    lect_list = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.lect_list.append(self)

    def mark_list(self, marks_):
        lis = []
        for i in marks_.values():
            for a in i:
                lis.append(a)
        return lis

    def __str__(self):

        person = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка: {sum(self.mark_list(self.grades)) / len(self.mark_list(self.grades))} \n'
        return person

    def __lt__(self, other):
        if isinstance(other, Lecture):
            avg_mark1 = sum(self.mark_list(self.grades)) / len(self.mark_list(self.grades))
            avg_mark2 = sum(other.mark_list(other.grades)) / len(other.mark_list(other.grades))
        return avg_mark1 < avg_mark2


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        person = f'Имя: {self.name} \nФамилия: {self.surname}'
        return person


best_student = Student('Ruoy', 'Eman', 'your_gender')
worse_student = Student('Joe', 'Biden', 'man')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
worse_student.courses_in_progress += ['Python']
worse_student.courses_in_progress += ['Git']
best_student.add_courses('Введение в программирование')
worse_student.add_courses('Введение в программирование')

cool_mentor = Reviewer('Some', 'Buddy')
bad_mentor = Reviewer('Some', 'One')
cool_mentor.courses_attached += ['Python']
bad_mentor.courses_attached += ['Git']

Anna_Petrova = Lecture('anna', 'petrova')
Olga_Ivanova = Lecture('olga', 'ivanova')
Olga_Ivanova.courses_attached += ['Git']
Olga_Ivanova.courses_attached += ['Python']
Anna_Petrova.courses_attached += ['Python']

bad_mentor.rate_hw(best_student, 'Git', 4)
bad_mentor.rate_hw(best_student, 'Git', 4)
bad_mentor.rate_hw(worse_student, 'Git', 3)
bad_mentor.rate_hw(worse_student, 'Git', 3)

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_mentor.rate_hw(worse_student, 'Python', 10)
cool_mentor.rate_hw(worse_student, 'Python', 9)
cool_mentor.rate_hw(worse_student, 'Python', 9)
cool_mentor.rate_hw(worse_student, 'Python', 9)

worse_student.rate_hw(Olga_Ivanova, 'Git', 8)
worse_student.rate_hw(Olga_Ivanova, 'Git', 7)
best_student.rate_hw(Olga_Ivanova, 'Python', 6)
worse_student.rate_hw(Anna_Petrova, 'Git', 8)
best_student.rate_hw(Anna_Petrova, 'Git', 7)
best_student.rate_hw(Anna_Petrova, 'Python', 6)

print(best_student)
print(worse_student)

print(cool_mentor)
print()
print(bad_mentor)
print()

print(Olga_Ivanova)
print(Anna_Petrova)

print(Olga_Ivanova < Anna_Petrova)
print(best_student > worse_student)
print()


def course_avg(stud_list_, course):
    x = 0
    y = 0
    for stud in Student.stud_list:
        if course in stud.courses_in_progress and course in stud.grades:
            x = x + sum(stud.grades[course]) / len(stud.grades[course])
            y += 1
    return x / y


print(f"Средняя оценка всех студентов по курсу Python: {course_avg(Student.stud_list, 'Python')}")


def lec_avg(lect_list_, course):
    x = 0
    y = 0
    for lect in Lecture.lect_list:
        if course in lect.courses_attached:
            x = x + sum(lect.grades[course]) / len(lect.grades[course])
            y += 1
    return x / y


print(f"Средняя оценка всех лекторов по курсу Git: {lec_avg(Lecture.lect_list, 'Git')}")