from operator import itemgetter, attrgetter, methodcaller

a = [1, -45, 3, 2, 100, -4]
a.sort()
print(a)

b = ("hello", "abc", "htftr")
print(sorted(b))
print(sorted("python"))

print(sorted([1, 0, -5, 10, 20], reverse=True))

d = {"c": "hello", "a": "python", "b": "py"}
print(sorted(d))
print(sorted(d.values()))
a_dict = dict(sorted(d.items()))
print(a_dict)

a_str = sorted("This is a test string from Andrew".split(), key=str.lower)
print(a_str)

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

print(sorted(student_tuples, key=lambda student: student[2]))


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

    def weighted_grade(self):
        return 'CBA'.index(self.grade) / self.age


student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

print(sorted(student_objects, key=lambda student: student.age))

print(sorted(student_tuples, key=itemgetter(2)))
print(sorted(student_objects, key=attrgetter('age')))

print(sorted(student_tuples, key=itemgetter(1, 2)))
print(sorted(student_objects, key=attrgetter('grade', 'age')))

print([(student.name, student.weighted_grade()) for student in student_objects])
print(sorted(student_objects, key=methodcaller('weighted_grade')))

data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
print(sorted(data, key=itemgetter(0)))

s = sorted(student_objects, key=attrgetter('age'))
print(sorted(s, key=attrgetter('grade'), reverse=True))
